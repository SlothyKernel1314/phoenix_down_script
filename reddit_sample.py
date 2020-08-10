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


def get_saved_posts(after_pagination=None, saved_posts_count=0,  all_datas=None):
    if all_datas is None:
        all_datas = []
    my_token = reddit_request_token()
    if after_pagination is None:
        url = "https://oauth.reddit.com/user/" + REDDIT_USERNAME.lower() + "/saved?limit=100"
    else:
        url = "https://oauth.reddit.com/user/" + REDDIT_USERNAME.lower() + "/saved?limit=100&after=" + after_pagination
    headers = {"Authorization": "bearer " + my_token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
    response = requests.get(url, headers=headers)
    current_datas = response.json()
    all_datas.append(current_datas)
    after_pagination = current_datas['data']['after']
    saved_posts_current_dist = current_datas['data']['dist']
    saved_posts_count += saved_posts_current_dist
    if after_pagination is not None:
        return get_saved_posts(after_pagination, saved_posts_count, all_datas)
    else:
        return all_datas, saved_posts_count


def get_subscribed_subreddits(after_pagination=None, subreddits_count=0, all_datas=None):
    if all_datas is None:
        all_datas = []
    my_token = reddit_request_token()
    if after_pagination is None:
        url = "https://oauth.reddit.com/subreddits/mine/subscriber?limit=100"
    else:
        url = "https://oauth.reddit.com/subreddits/mine/subscriber?limit=100&after=" + after_pagination
    headers = {"Authorization": "bearer " + my_token, "User-Agent": "phoenix-down/0.1 by IAmTerror"}
    response = requests.get(url, headers=headers)
    current_datas = response.json()
    all_datas.append(current_datas)
    after_pagination = current_datas['data']['after']
    subreddits_current_dist = current_datas['data']['dist']
    subreddits_count += subreddits_current_dist
    if after_pagination is not None:
        return get_subscribed_subreddits(after_pagination, subreddits_count, all_datas)
    else:
        return all_datas, subreddits_count

