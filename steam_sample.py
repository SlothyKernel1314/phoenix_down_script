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


# WARNING : intensive time-based function because shitty Steam API provides a buggy GetGlobalStatsForGame method...
# ... so we must use a trick, we get instead all Steam games list, and pick the desired game inside.
def get_game_name_by_id(id):
    game_name = ""
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"  # returns ALL Steam games
    response = requests.request("GET", url)
    datas = response.json()
    games_list = datas['applist']['apps']
    for game in games_list:
        if game['appid'] == id:
            game_name = game['name']
    return game_name


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
    print(datas)
    games = datas['response']['games']
    for game in games:
        game_id = game['appid']
        print(game_id)


def get_wishlist():
    # we set an arbitrarily high number of pages because...
    # ...the shitty Steam API doesn't provide methods to correctly get the wishlist of steam users
    number_of_pages_limit = 20
    current_page = 0
    number_of_games_in_wishlist = 0
    while current_page < number_of_pages_limit:
        url = "https://store.steampowered.com/wishlist/profiles/" + STEAM_USER_ID +\
              "/wishlistdata/?p=" + str(current_page) + ""
        response = requests.request("GET", url)
        datas = response.json()
        current_page += 1
        if len(datas) > 0:
            print(datas)
            print(len(datas))
            number_of_games_in_wishlist += len(datas)
        else:
            break
    print("Number of games in the wishlist : " + str(number_of_games_in_wishlist))


