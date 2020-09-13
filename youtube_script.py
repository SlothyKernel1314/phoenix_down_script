# -*- coding: utf-8 -*-
# !/usr/bin/env python

from utilities import *
from constants import *
import os
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.errors import HttpError
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class YoutubeScript:
    def __init__(self):
        self.application_name = "youtube"

    @staticmethod
    def get_authenticated_service():
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = YOUTUBE_CLIENT_SECRETS_FILE
        credential_path = os.path.join(PD_SCRIPT_ROOT_APP_PATH + '/', YOUTUBE_CREDENTIAL_JSON)
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
            credentials = tools.run_flow(flow, store)
        return googleapiclient.discovery.build(api_service_name, api_version,
                                               credentials=credentials, cache_discovery=False)

    def get_my_subscriptions(self, next_page_token=None, all_datas=None):
        if all_datas is None:
            all_datas = []
        youtube = self.get_authenticated_service()
        request = youtube.subscriptions().list(
            part="snippet,contentDetails",
            maxResults=50,
            mine=True,
            pageToken=None if next_page_token is None else next_page_token
        )
        try:
            response = request.execute()
            all_datas.append(response)
            if 'nextPageToken' in response:
                next_page_token = response['nextPageToken']
            nb_suscriptions = response['pageInfo']['totalResults']
            if 'nextPageToken' in response and next_page_token is not None:
                return self.get_my_subscriptions(next_page_token, all_datas)
            else:
                return all_datas, nb_suscriptions
        except HttpError as e:
            logging.warning("Error: " + str(e))

    def get_playlists_by_channel_id_with_exceptions(self, channel_id):
        youtube = self.get_authenticated_service()
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
        )
        try:
            response = request.execute()
            items = response['items'][0]
            playlists = items['contentDetails']['relatedPlaylists']
            # remove useless playlists
            playlists.pop('likes')
            playlists.pop('uploads')
            playlists.pop('watchHistory')
            playlists.pop('watchLater')
            # add a playlist that is not detected by the method get_playlists_by_channel_id_with_exceptions()
            playlists["later"] = YOUTUBE_USER_PLAYLIST_LATER_ID
            return playlists
        except HttpError as e:
            logging.warning("Error: " + str(e))

    def get_playlist_items_by_playlist_id(self, playlist_id, next_page_token=None, all_datas=None):
        if all_datas is None:
            all_datas = []
        youtube = self.get_authenticated_service()
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=50,
            playlistId=playlist_id,
            pageToken=None if next_page_token is None else next_page_token
        )
        try:
            response = request.execute()
            all_datas.append(response)
            if 'nextPageToken' in response:
                next_page_token = response['nextPageToken']
            nb_suscriptions = response['pageInfo']['totalResults']
            if 'nextPageToken' in response and next_page_token is not None:
                return self.get_playlist_items_by_playlist_id(playlist_id, next_page_token, all_datas)
            else:
                return all_datas, nb_suscriptions
        except HttpError as e:
            logging.warning("Error: " + str(e))

    def run_script(self):
        logging.info('youtube script is running...')

        create_directory(PD_SCRIPT_ROOT_LOGS_PATH + "/" + self.application_name)

        my_subscriptions = self.get_my_subscriptions()

        my_playlists = self.get_playlists_by_channel_id_with_exceptions(YOUTUBE_USER_ID)

        logging.info('creating youtube log file')
        file_name = create_timestamped_and_named_file_name(self.application_name)
        file = open(file_name, "w", encoding="utf-8")

        logging.info('writing in youtube log file...')
        # processing of youtube subscriptions
        file.write("##### Youtube subscriptions of BigBossFF user (list) :")
        file.write("\n\n")
        if my_subscriptions is not None:
            my_subscriptions_all_datas = my_subscriptions[0]
            my_subscriptions_count = my_subscriptions[1]
            for json in my_subscriptions_all_datas:
                items = json['items']
                for item in items:
                    channel_id = item['snippet']['resourceId']['channelId']
                    channel_title = item['snippet']['title']
                    file.write(channel_id + " ----- " + channel_title)
                    file.write("\n")
            file.write("\n\n")
            file.write("BigBossFF Youtube user have " + str(my_subscriptions_count) + " suscribed channels")
            file.write("\n\n\n\n")
            file.write("##### Youtube subscriptions of BigBossFF user (JSON) :")
            file.write("\n\n")
            for json in my_subscriptions_all_datas:
                file.write(str(json))
                file.write("\n\n\n\n")
            file.write("\n\n\n\n")
        # processing of youtube playlists
        file.write("##### Youtube playlists of BigBossFF user :")
        if my_playlists is not None:
            for playlist in my_playlists:
                file.write("\n\n")
                file.write("### Playlist : " + playlist + " (list)")
                file.write("\n\n")
                playlist_content_all_datas = self.get_playlist_items_by_playlist_id(my_playlists[playlist])
                if playlist_content_all_datas is not None:
                    for json in playlist_content_all_datas[0]:
                        items = json['items']
                        for item in items:
                            item_id = item['snippet']['resourceId']['videoId']
                            item_title = item['snippet']['title']
                            file.write(item_id + " ----- " + item_title)
                            file.write("\n")
                    file.write("\n\n")
                    file.write("### Playlist : " + playlist + " (JSON)")
                    for json in playlist_content_all_datas[0]:
                        file.write("\n\n")
                        file.write(str(json))
                        file.write("\n\n")
                    file.write("There are " + str(playlist_content_all_datas[1]) +
                               " videos in " + playlist.capitalize() + " playlist")
                    file.write("\n\n\n\n")

        logging.info('writing in youtube log file done')
        file.close()

        # opens the file for reading only in binary format in order to upload
        file = open(file_name, "rb")

        upload_file_to_server_ftp(file, file_name, self.application_name)

        file.close()

        logging.info('youtube script is terminated')










