# -*- coding: utf-8 -*-
# !/usr/bin/env python

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import httplib2
import oauth2_client
from oauth2client import client
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "/mnt/C26C9CBE6C9CAF23/OUTER_HEAVEN/projects/sysscripts/" \
                          "phoenix_down_script/client_secret.json"

    # # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials, cache_discovery=False)

    def get_authenticated_service(): # Modified
        credential_path = os.path.join('./', 'credential_sample.json')
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
            credentials = tools.run_flow(flow, store)
        return googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    youtube = get_authenticated_service()

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()

    print(response)