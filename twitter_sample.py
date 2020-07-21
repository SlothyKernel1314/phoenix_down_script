# -*- coding: utf-8 -*-
# !/usr/bin/env python

import tweepy
from credentials import *

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def get_timeline():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


def update_status():  # also known as... tweeting
    tweet = "Bonjour, c'est pas moi qui tweete, c'est un robot, fais pas attention, je vais disparaitre d'ici peu..."
    try:
        api.update_status(tweet)
        print("the tweet was posted !")
    except tweepy.error.RateLimitError:
        print("fail due to hitting Twitter’s rate limit !")
    except tweepy.error.TweepError:
        print("failed tweting !")


def get_user_by_id(user_id):
    user_information = api.get_user(user_id)
    print(user_information)


# WARNING : Rate limit window per 15 minutes = 15 requests x 20 followers per page = 300 followers
def get_followers(user_id):
    user_information = api.get_user(user_id)
    nb_followers = user_information.followers_count
    print("L'utilisateur " + user_information.screen_name + " a " + str(nb_followers) + " followers")
    try:
        for follower in tweepy.Cursor(api.followers, user_id).items(nb_followers):
            print(follower.screen_name)
    except tweepy.RateLimitError as e:
        print(e)


def get_followers_id(user_id):
    user_followers = api.followers_ids(user_id)
    print(user_followers)
    print(len(user_followers))


def get_friends_id(user_id):
    user_friends = api.friends_ids(user_id)
    print(user_friends)
    print(len(user_friends))


# WARNING : very long processing time
def get_all_tweets_for_a_user(user_id):
    count = 0
    for tweet in tweepy.Cursor(api.user_timeline, id=user_id).items():
        print(tweet)
        count += 1
    print(count)


def get_rate_limit_status():
    rate_limit_status = api.rate_limit_status()
    print(rate_limit_status)


