# -*- coding: utf-8 -*-
# !/usr/bin/env python

from utilities import *
from credentials import *
from constants import *
import tweepy


class TwitterScript:

    def __init__(self):
        self.application_name = "twitter"
        self.auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    @staticmethod
    def get_user_by_id(user_id, api):
        try:
            user_information = api.get_user(user_id)
        except tweepy.TweepError as e:
            logging.warning("Error: " + str(e))
            user_information = ""
        return user_information

    @staticmethod
    def get_followers_id(user_id, api):
        try:
            user_followers = api.followers_ids(user_id)
        except tweepy.TweepError as e:
            logging.warning("Error: " + str(e))
            user_followers = ""
        return user_followers

    @staticmethod
    def get_friends_id(user_id, api):
        try:
            user_friends = api.friends_ids(user_id)
        except tweepy.TweepError as e:
            logging.warning("Error: " + str(e))
            user_friends = ""
        return user_friends

    def run_script(self):

        logging.info('twitter script is running...')

        create_directory(PD_SCRIPT_ROOT_LOGS_PATH + "/" + self.application_name)

        api = self.api

        user = self.get_user_by_id(TWITTER_USER_ID, api)

        followers = self.get_followers_id(TWITTER_USER_ID, api)

        friends = self.get_friends_id(TWITTER_USER_ID, api)

        logging.info('creating twitter log file')
        file_name = create_timestamped_and_named_file_name(self.application_name)
        file = open(file_name, "w", encoding="utf-8")

        logging.info('writing in twitter log file...')
        # processing of followers
        if len(str(user)) > 0 and len(str(followers)) > 0:
            file.write(user.screen_name + " twitter user have " + str(len(followers)) + " followers")
            file.write("\n\n")
            file.write("List of followers' ids of " + user.screen_name + " : \n")
        for follower in followers:
            file.write(str(follower))
            file.write("\n")
        file.write("\n\n\n\n")
        # processing of friends
        if len(str(user)) > 0 and len(str(friends)) > 0:
            file.write(user.screen_name + " twitter user have " + str(len(friends)) + " friends")
            file.write("\n\n")
            file.write("List of friends' ids of " + user.screen_name + " : \n")
        for friend in friends:
            file.write(str(friend))
            file.write("\n")

        logging.info('writing in twitter log file done')
        file.close()

        # opens the file for reading only in binary format in order to upload
        file = open(file_name, "rb")

        upload_file_to_server_ftp(file, file_name, self.application_name)

        file.close()

        logging.info('twitter script is terminated')



