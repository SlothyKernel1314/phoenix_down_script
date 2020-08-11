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
    return response

