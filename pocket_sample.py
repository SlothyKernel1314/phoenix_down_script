# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
from constants import *
import requests
import requests.auth


def pocket_request_token():
    url = "https://getpocket.com/v3/oauth/request"
    payload = {"consumer_key": POCKET_CONSUMER_KEY,
               "redirect_uri":"pocketapp1234:authorizationFinished"}
    response = requests.request("POST", url, params=payload)
    datas = response.text
    split_datas = datas.split("=")
    request_token = split_datas[1]
    return request_token


def authorize_app():
    code = pocket_request_token()
    url = "https://getpocket.com/auth/authorize?request_token=" \
          + code + "&redirect_uri=pocketapp1234:authorizationFinished"
    print(url)


# def get_pocket_access_token():
#     code = pocket_request_token()
#     print(code)
#     url = "https://getpocket.com/v3/oauth/authorize"
#     payload = {"consumer_key": POCKET_CONSUMER_KEY,
#                "code": code}
#     response = requests.request("POST", url, params=payload)
#     print(response)

