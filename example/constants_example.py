# -*- coding: utf-8 -*-
# !/usr/bin/env python

# CONFIGURATION VARIABLES (Requires a choice by the user !) ------------------------------------------------------------

# Directory where you run this application
PD_SCRIPT_ROOT_APP_PATH = "../"
# Directory where you want to save (locally) your logs
PD_SCRIPT_ROOT_LOGS_PATH = "../"

# Directory where you upload logs
SEEDBOX_ROOT_PD_SCRIPT_PATH = "../"

# Examples of boards and Trello labels. Rename according to your own needs, or disable alerts.py if...
# ... you don't want to be alerted via Trello of a script execution error.
# Read the Trello API documentation for more information.
TRELLO_MEMBER_USERNAME = ""
TRELLO_CARDS_IDS = ['', '', '']
TRELLO_MBL_BOARD_ADMIN_LIST_ID = ""
TRELLO_ALERT_BOARD_ALERT_LIST_ID = ""
TRELLO_MBL_URGENT_CUSTOM_LABEL_ID = ""
TRELLO_ALERT_URGENT_CUSTOM_LABEL_ID = ""

FIREFOX_PROFILE_DIRECTORY_PATH = ".../.mozilla/firefox/xxxxxxxxxx.default"
FIREFOX_BOOKMARKBACKUPS_FOLDER = "bookmarkbackups"
FIREFOX_PLACES_SQLITE_FILE_NAME = "places.sqlite"
FIREFOX_FAVICONS_SQLITE_FILE_NAME = "favicons.sqlite"
FIREFOX_ZIP_FILE_BASENAME = "firefox_backup"

JDOWNLOADER_CFG_DIRECTORY_PATH = "../jd2/cfg"
JDOWNLOADER_ZIP_FILE_BASENAME = "jdownloader_cfg_partial_backup"

PD_SCRIPT_STARTING_MESSAGE = 'Phoenix Down Script started !'
PD_SCRIPT_ENDING_MESSAGE = 'Phoenix Down Script finished !'

TWITTER_USER_ID = ""

STEAM_USER_ID = ""

YOUTUBE_USER_ID = ""
YOUTUBE_USER_PLAYLIST_LATER_ID = ""  # a custom playlist
YOUTUBE_CREDENTIAL_JSON = 'youtube_credential.json'
YOUTUBE_CLIENT_SECRETS_FILE_PATH = "../client_secret.json"
