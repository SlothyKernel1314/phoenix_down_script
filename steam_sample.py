# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
from constants import *
import requests


def get_user_name(id):
    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + STEAM_API_KEY + \
          "&steamids=" + id
    response = requests.request("GET", url)
    users = response.json()
    # Steam API returns a list of ONE user when we call GetPlayerSummaries API method...
    # ... so we must parse this list, even if there is only one user in it
    for user in users['response']['players']:
        user_name = user['personaname']
        print(user_name)
    return user_name


def get_friend_list():
    url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + STEAM_API_KEY + \
          "&steamid=" + STEAM_USER_ID + "&relationship=friend"

    response = requests.request("GET", url)
    friends = response.json()
    for friend in friends['friendslist']['friends']:
        friend_id = friend['steamid']
        print(friend_id)
