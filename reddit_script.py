# -*- coding: utf-8 -*-
# !/usr/bin/env python

from utilities import *
from credentials import *
from constants import *
import requests
import requests
import requests.auth

# Oath2 Reddit quick start : https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
# Oath2 Reddit documentation : https://github.com/reddit-archive/reddit/wiki/OAuth2


class RedditScript:
    def __init__(self):
        self.application_name = "reddit"

    def reddit_request_token(self):
        client_auth = requests.auth.HTTPBasicAuth(REDDIT_APP_CLIENT_KEY, REDDIT_API_SECRET_KEY)
        post_data = {"grant_type": "password", "username": REDDIT_USERNAME, "password": REDDIT_PASSWORD}
        headers = {"User-Agent": "phoenix-down/0.1 by IAmTerror"}
        response = requests.post("https://www.reddit.com/api/v1/access_token",
                             auth=client_auth, data=post_data, headers=headers)
        datas = response.json()
        token = datas['access_token']
        return token

    def get_username(self):
        my_token = self.reddit_request_token()
        url = "https://oauth.reddit.com/api/v1/me"
        headers = {"Authorization": "bearer " + my_token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
        response = requests.get(url, headers=headers)
        datas = response.json()
        username = datas['name']
        return username

    def run_script(self):
        logging.info('reddit script is running...')

        create_directory(PD_SCRIPT_ROOT_PATH + "/" + self.application_name)

        username = self.get_username()

        logging.info('creating reddit log file')
        file_name = create_timestamped_and_named_file_name(self.application_name)
        file = open(file_name, "w", encoding="utf-8")

        logging.info('writing in reddit log file...')
        # processing of saved posts
        file.write("##### Saved posts of " + username + " reddit user :")
