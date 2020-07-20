from utilities import *
from credentials import *
from constants import *
import tweepy


class TwitterScript:

    def __init__(self, api):
        self.application_name = "twitter"
        self.auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def run_script(self):
        pass
