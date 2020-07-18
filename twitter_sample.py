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
        print("tweet posté !")
    except tweepy.error.TweepError:
        print("échec de l'envoi du tweet !")
