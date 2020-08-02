# -*- coding: utf-8 -*-
# !/usr/bin/env python

from utilities import *
from credentials import *
from constants import *
import requests
import os


class SteamScript:
    def __init__(self):
        self.application_name = "steam"

    def get_user_name(self, id):
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + STEAM_API_KEY + \
              "&steamids=" + id
        response = requests.request("GET", url)
        datas = response.json()
        users = datas['response']
        user = users['players']
        # Steam API returns a list of ONE user when we call GetPlayerSummaries API method, so...
        user_name = user[0]['personaname']
        return user_name

    def get_friend_list(self):
        url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + STEAM_API_KEY + \
              "&steamid=" + STEAM_USER_ID + "&relationship=friend"
        friends_dictionnary = {}
        response = requests.request("GET", url)
        friends = response.json()
        for friend in friends['friendslist']['friends']:
            friend_id = friend['steamid']
            friend_user_name = self.get_user_name(friend_id)
            friends_dictionnary[friend_id] = friend_user_name
        return friends_dictionnary

    def get_owned_games_ids(self):
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + STEAM_API_KEY + \
              "&steamid=" + STEAM_USER_ID + "&format=json"
        my_games_ids = []
        response = requests.request("GET", url)
        datas = response.json()
        my_games = datas['response']['games']
        for game in my_games:
            my_games_ids.append(game['appid'])
        return my_games_ids

    def get_wishlist(self):
        # we set an arbitrarily high number of pages because...
        # ...the shitty Steam API doesn't provide methods to correctly get the wishlist of steam users
        number_of_pages_limit = 20
        current_page = 0
        number_of_games_in_wishlist = 0
        custom_wishlist_datas = []
        while current_page < number_of_pages_limit:
            url = "https://store.steampowered.com/wishlist/profiles/" + STEAM_USER_ID + \
                  "/wishlistdata/?p=" + str(current_page) + ""
            response = requests.request("GET", url)
            datas = response.json()
            current_page += 1
            if len(datas) > 0:
                custom_wishlist_datas.append("Page " + str(current_page) + " : " + str(datas))
                number_of_games_in_wishlist += len(datas)
            else:
                break
        return custom_wishlist_datas, number_of_games_in_wishlist

    def run_script(self):

        logging.info('steam script is running...')

        create_directory(PD_SCRIPT_ROOT_PATH + "/" + self.application_name)

        user = self.get_user_name(STEAM_USER_ID)

        friends = self.get_friend_list()

        my_games_ids = self.get_owned_games_ids()

        wishlist = self.get_wishlist()
        custom_wishlist_datas = wishlist[0]

        logging.info('creating steam log file')
        file_name = create_timestamped_and_named_file_name(self.application_name)
        file = open(file_name, "w", encoding="utf-8")

        logging.info('writing in steam log file...')
        # processing of friends
        file.write("##### Friends list of " + user + " steam user :")
        file.write("\n\n")
        file.write(str(friends))
        file.write("\n\n")
        for key, value in friends.items():
            file.write(key + " --- " + value)
            file.write("\n")
        file.write("\n")
        file.write(user + " steam user have " + str(len(friends)) + " friends on steam")
        file.write("\n\n\n\n")
        # processing of owned games
        file.write("##### " + user + " owned games ids :")
        file.write("\n\n")
        file.write(str(my_games_ids))
        file.write("\n\n")
        file.write(user + " steam user have " + str(len(my_games_ids)) + " games on steam")
        file.write("\n\n\n\n")
        # processing of wishlist
        file.write("##### " + user + " wishlist :")
        file.write("\n\n")
        for page in custom_wishlist_datas:
            file.write(str(page))
            file.write("\n\n")
        file.write(user + " steam user have " + str(wishlist[1]) + " games in his wishlist")

        logging.info('writing in steam log file done')
        file.close()

        # opens the file for reading only in binary format in order to upload
        file = open(file_name, "rb")

        upload_file_to_server_ftp(file, file_name, self.application_name)

        file.close()

        logging.info('steam script is terminated')


