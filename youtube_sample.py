# -*- coding: utf-8 -*-
# !/usr/bin/env python

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from constants import *


def get_authenticated_service():
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "/mnt/C26C9CBE6C9CAF23/OUTER_HEAVEN/projects/sysscripts/" \
                          "phoenix_down_script/client_secret.json"
    # TODO : transformer en constante pour déploiement plus facile
    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
        credentials = tools.run_flow(flow, store)
    return googleapiclient.discovery.build(api_service_name, api_version,
                                           credentials=credentials, cache_discovery=False)


def get_channel_details_by_channel_id(channel_id):
    youtube = get_authenticated_service()
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()
    print(response)
    return response


def get_my_subscriptions(next_page_token=None, all_datas=None):
    if all_datas is None:
        all_datas = []
    youtube = get_authenticated_service()
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
        return get_my_subscriptions(next_page_token, all_datas)
    else:
        print(all_datas)
        return all_datas, nb_suscriptions


def get_playlists_by_channel_id(channel_id):
    youtube = get_authenticated_service()
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()
    items = response['items'][0]
    dictionnary_of_playlists_names_with_their_ids = items['contentDetails']['relatedPlaylists']
    print(dictionnary_of_playlists_names_with_their_ids)
    return dictionnary_of_playlists_names_with_their_ids


def get_playlist_items_by_playlist_id(playlist_id, next_page_token=None, all_datas=None):
    if all_datas is None:
        all_datas = []
    youtube = get_authenticated_service()
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=50,
        playlistId=playlist_id,
        pageToken=None if next_page_token is None else next_page_token
    )
    response = request.execute()
    all_datas.append(response)
    if 'nextPageToken' in response:
        next_page_token = response['nextPageToken']
    nb_suscriptions = response['pageInfo']['totalResults']
    if 'nextPageToken' in response and next_page_token is not None:
        return get_playlist_items_by_playlist_id(playlist_id, next_page_token, all_datas)
    else:
        print(all_datas)
        return all_datas, nb_suscriptions



