# -*- coding: utf-8 -*-
# !/usr/bin/env python

from utilities import *
from manager.credentials_manager import *
from manager.constants_manager import *
import requests
import requests.auth


class RedditScript:
    def __init__(self):
        self.application_name = "reddit"

    @staticmethod
    def reddit_request_token():
        client_auth = requests.auth.HTTPBasicAuth(REDDIT_APP_CLIENT_KEY, REDDIT_API_SECRET_KEY)
        post_data = {"grant_type": "password", "username": REDDIT_USERNAME, "password": REDDIT_PASSWORD}
        headers = {"User-Agent": "phoenix-down/0.1 by IAmTerror"}
        try:
            response = requests.post("https://www.reddit.com/api/v1/access_token",
                                     auth=client_auth, data=post_data, headers=headers)
            try:
                response.raise_for_status()
                datas = response.json()
                token = datas['access_token']
            except requests.exceptions.HTTPError as e:
                logging.warning("Error: " + str(e))
                token = ""
        except Exception as e:
            logging.warning("Error: " + str(e))
            token = ""
        return token

    @staticmethod
    def get_username(token):
        url = "https://oauth.reddit.com/api/v1/me"
        headers = {"Authorization": "bearer " + token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
        response = requests.get(url, headers=headers)
        try:
            response.raise_for_status()
            datas = response.json()
            username = datas['name']
        except requests.exceptions.HTTPError as e:
            logging.warning("Error: " + str(e))
            username = ""
        return username

    def get_saved_posts(self, token, after_pagination=None, saved_posts_count=0, all_datas=None):
        if all_datas is None:
            all_datas = []
        if after_pagination is None:
            url = "https://oauth.reddit.com/user/" + REDDIT_USERNAME.lower() + "/saved?limit=100"
        else:
            url = "https://oauth.reddit.com/user/" + REDDIT_USERNAME.lower() \
                  + "/saved?limit=100&after=" + after_pagination
        headers = {"Authorization": "bearer " + token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
        response = requests.get(url, headers=headers)
        try:
            response.raise_for_status()
            current_datas = response.json()
            all_datas.append(current_datas)
            after_pagination = current_datas['data']['after']
            saved_posts_current_dist = current_datas['data']['dist']
            saved_posts_count += saved_posts_current_dist
            if after_pagination is not None:
                return self.get_saved_posts(token, after_pagination, saved_posts_count, all_datas)
            else:
                return all_datas, saved_posts_count
        except requests.exceptions.HTTPError as e:
            logging.warning("Error: " + str(e))

    def get_subscribed_subreddits(self, token, after_pagination=None, subreddits_count=0, all_datas=None):
        if all_datas is None:
            all_datas = []
        if after_pagination is None:
            url = "https://oauth.reddit.com/subreddits/mine/subscriber?limit=100"
        else:
            url = "https://oauth.reddit.com/subreddits/mine/subscriber?limit=100&after=" + after_pagination
        headers = {"Authorization": "bearer " + token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
        response = requests.get(url, headers=headers)
        try:
            response.raise_for_status()
            current_datas = response.json()
            all_datas.append(current_datas)
            after_pagination = current_datas['data']['after']
            subreddits_current_dist = current_datas['data']['dist']
            subreddits_count += subreddits_current_dist
            if after_pagination is not None:
                return self.get_subscribed_subreddits(token, after_pagination, subreddits_count, all_datas)
            else:
                return all_datas, subreddits_count
        except requests.exceptions.HTTPError as e:
            logging.warning("Error: " + str(e))

    def run_script(self):
        logging.info('reddit script is running...')

        create_directory(PD_SCRIPT_ROOT_LOGS_PATH + "/" + self.application_name)

        token = self.reddit_request_token()

        if len(token) > 0:

            username = self.get_username(token)

            saved_posts = self.get_saved_posts(token)

            suscribed_subreddits = self.get_subscribed_subreddits(token)

            logging.info('creating reddit log file')
            file_name = create_timestamped_and_named_file_name(self.application_name)
            file = open(file_name, "w", encoding="utf-8")

            logging.info('writing in reddit log file...')
            # processing of saved posts
            file.write("##### Saved posts of " + username + " reddit user (JSON) :")
            file.write("\n\n")
            if saved_posts is not None:
                file.write(username + " reddit user have " + str(saved_posts[1]) + " saved posts")
                file.write("\n\n")
                for json in saved_posts[0]:
                    file.write(str(json))
                    file.write("\n\n\n\n")
            # processing of subreddits
            file.write("##### Suscribed subreddits of " + username + " reddit user (list) :")
            file.write("\n\n")
            if suscribed_subreddits is not None:
                file.write(username + " reddit user have " + str(suscribed_subreddits[1]) + " suscribed subreddits")
                file.write("\n\n")
                for json in suscribed_subreddits[0]:
                    children = json['data']['children']
                    for subreddit in children:
                        file.write(subreddit['data']['display_name_prefixed'])
                        file.write("\n")
                file.write("\n\n")
                file.write("##### Suscribed subreddits of " + username + " reddit user (JSON) :")
                file.write("\n\n")
                for json in suscribed_subreddits[0]:
                    file.write(str(json))
                    file.write("\n\n\n\n")

            logging.info('writing in reddit log file done')
            file.close()

            # opens the file for reading only in binary format in order to upload
            file = open(file_name, "rb")

            upload_file_to_server_ftp(file, file_name, self.application_name)

            file.close()

        logging.info('reddit script is terminated')
