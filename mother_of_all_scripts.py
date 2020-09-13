# !/usr/bin/python
# -*- coding: utf-8 -*-

from script.trello_script import *
from script.firefox_script import *
from script.jdownloader_script import *
from script.twitter_script import *
from script.steam_script import *
from script.reddit_script import *
from script.pocket_script import *
from script.youtube_script import *
from logger_setup import *


# MAIN SCRIPT ----------------------------------------------------------------------------------------------------------

def mother_of_all_scripts():

    logging.info("creating the root path directory of Phoenix Down Script...")
    create_directory(PD_SCRIPT_ROOT_LOGS_PATH)

    tlls = TrelloScript()
    tlls.run_script()

    # fs = FirefoxScript()
    # fs.run_script()
    #
    # js = JdownloaderScript()
    # js.run_script()
    #
    # twts = TwitterScript()
    # twts.run_script()
    #
    # stms = SteamScript()
    # stms.run_script()
    #
    # rs = RedditScript()
    # rs.run_script()
    #
    # ps = PocketScript()
    # ps.run_script()
    #
    # ys = YoutubeScript()
    # ys.run_script()


# SAMPLE REQUESTS ------------------------------------------------------------------------------------------------------

# TRELLO SAMPLE
# get_board_by_id(TRELLO_MBL_BOARD_ID)
# get_open_cards_by_board_id(TRELLO_MBL_BOARD_ID)
# get_card_by_id(TRELLO_CH_CARD_ID)
# get_boards_by_member_username(TRELLO_MEMBER_USERNAME)
# get_lists_on_a_board(TRELLO_MBL_BOARD_ID)
# get_lists_on_a_board(TRELLO_ALERT_BOARD_ID)
# get_labels_on_a_board(TRELLO_MBL_BOARD_ID)
# get_labels_on_a_board(TRELLO_ALERT_BOARD_ID)
# create_a_new_card(TRELLO_MBL_BOARD_ADMIN_LIST_ID, TRELLO_MBL_URGENT_CUSTOM_LABEL_ID)
# create_a_new_card(TRELLO_ALERT_BOARD_ALERT_LIST_ID, TRELLO_ALERT_URGENT_CUSTOM_LABEL_ID)

# TWITTER SAMPLE
# get_timeline()
# update_status()
# get_user_by_id(TWITTER_USER_ID)
# get_followers_id(TWITTER_USER_ID)
# get_friends_id(TWITTER_USER_ID)
# get_all_tweets_for_a_user(TWITTER_USER_ID) # WARNING : very long processing time
# get_rate_limit_status()
# WARNING : Rate limit window per 15 minutes = 15 requests x 20 followers per page = 300 followers
# get_followers(TWITTER_USER_ID)

# STEAM SAMPLE
# get_user_name(STEAM_USER_ID)
# get_game_name_by_id(546560) # Half-Life : Alyx AppId
# get_friend_list()
# get_owned_games()
# get_wishlist()

# REDDIT SAMPLE
# reddit_request_token()
# get_my_identity()
# get_saved_posts()
# get_subscribed_subreddits()

# POCKET SAMPLE
# pocket_request_token()
# authorize_app()
# get_pocket_access_token()
# authorize_app_and_get_access_token()
# get_user_datas()

# YOUTUBE SAMPLE
# get_channel_details_by_channel_id(YOUTUBE_USER_ID)
# get_my_subscriptions()
# get_playlists_by_channel_id(YOUTUBE_USER_ID)
# get_playlist_items_by_playlist_id(YOUTUBE_USER_PLAYLIST_FAVORITES_ID)



