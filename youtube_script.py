# -*- coding: utf-8 -*-
# !/usr/bin/env python
import json

from utilities import *
from constants import *
import os
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class YoutubeScript:
    def __init__(self):
        self.application_name = "youtube"

    def get_authenticated_service(self):
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = YOUTUBE_CLIENT_SECRETS_FILE
        # TODO : modifier le chemin + constante
        credential_path = os.path.join('./', 'credential_sample.json')
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
        response = request.execute()
        all_datas.append(response)
        if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
        nb_suscriptions = response['pageInfo']['totalResults']
        if 'nextPageToken' in response and next_page_token is not None:
            return self.get_my_subscriptions(next_page_token, all_datas)
        else:
            return all_datas, nb_suscriptions

    def run_script(self):
        logging.info('youtube script is running...')

        create_directory(PD_SCRIPT_ROOT_PATH + "/" + self.application_name)

        my_subscriptions = self.get_my_subscriptions()
        my_subscriptions_all_datas = my_subscriptions[0]
        my_subscriptions_count = my_subscriptions[1]

        logging.info('creating youtube log file')
        file_name = create_timestamped_and_named_file_name(self.application_name)
        file = open(file_name, "w", encoding="utf-8")

        logging.info('writing in youtube log file...')
        # processing of youtube subscriptions
        file.write("##### Youtube subscriptions of BigBossFF user (list) :")
        file.write("\n\n")
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
        for json in my_subscriptions_all_datas:
            file.write(str(json))
            file.write("\n\n\n\n")
        file.write("\n\n\n\n")







