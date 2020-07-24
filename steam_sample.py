# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
from constants import *
import requests


def get_friend_list():
    url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + STEAM_API_KEY + \
          "&steamid=" + STEAM_USER_ID + "&relationship=friend"

    response = requests.request("GET", url)
    print(response.text)
