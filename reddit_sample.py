# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
from constants import *
import requests
import requests.auth

# Oath2 Reddit quick start : https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
# Oath2 Reddit documentation : https://github.com/reddit-archive/reddit/wiki/OAuth2


def reddit_request_token():
    client_auth = requests.auth.HTTPBasicAuth(REDDIT_APP_CLIENT_KEY, REDDIT_API_SECRET_KEY)
    post_data = {"grant_type": "password", "username": REDDIT_USERNAME, "password": REDDIT_PASSWORD}
    headers = {"User-Agent": "phoenix-down/0.1 by IAmTerror"}
    response = requests.post("https://www.reddit.com/api/v1/access_token",
                             auth=client_auth, data=post_data, headers=headers)
    datas = response.json()
    token = datas['access_token']
    return token


def get_my_identity():
    my_token = reddit_request_token()
    url = "https://oauth.reddit.com/api/v1/me"
    headers = {"Authorization": "bearer " + my_token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
    response = requests.get(url, headers=headers)
    datas = response.json()
    return datas


def get_saved_posts():
    my_token = reddit_request_token()
    url = "https://oauth.reddit.com/user/" + REDDIT_USERNAME.lower() + "/saved"
    headers = {"Authorization": "bearer " + my_token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
    response = requests.get(url, headers=headers)
    datas = response.json()
    return datas


def get_subscribed_subreddits():
    # TODO : pagination + recursive
    my_token = reddit_request_token()
    url = "https://oauth.reddit.com/subreddits/mine/subscriber?limit=80"
    headers = {"Authorization": "bearer " + my_token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
    response = requests.get(url, headers=headers)
    datas = response.json()
    print(datas)
    return datas

