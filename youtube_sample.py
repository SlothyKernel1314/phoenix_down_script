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


def get_authenticated_service():
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "/mnt/C26C9CBE6C9CAF23/OUTER_HEAVEN/projects/sysscripts/" \
                          "phoenix_down_script/client_secret.json"
    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
        credentials = tools.run_flow(flow, store)
    return googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)


def get_channel_by_id(channel_id):
    youtube = get_authenticated_service()
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()
    print(response)
    return response
