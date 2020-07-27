# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
from constants import *
import requests


def get_user_name(id):
    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + STEAM_API_KEY + \
          "&steamids=" + id
    response = requests.request("GET", url)
    datas = response.json()
    users = datas['response']
    user = users['players']
    # Steam API returns a list of ONE user when we call GetPlayerSummaries API method, so...
    user_name = user[0]['personaname']
    return user_name


def get_friend_list():
    url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + STEAM_API_KEY + \
          "&steamid=" + STEAM_USER_ID + "&relationship=friend"
    response = requests.request("GET", url)
    friends = response.json()
    for friend in friends['friendslist']['friends']:
        friend_id = friend['steamid']
        friend_user_name = get_user_name(friend_id)
        print(friend_id + " --- " + friend_user_name)


def get_owned_games():
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + STEAM_API_KEY +\
          "&steamid=" + STEAM_USER_ID + "&format=json"
    response = requests.request("GET", url)
    datas = response.json()
    games = datas['response']['games']
    for game in games:
        game_id = game['appid']
        print(game_id)
