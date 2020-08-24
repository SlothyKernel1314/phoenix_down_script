# -*- coding: utf-8 -*-
# !/usr/bin/env python

import requests
import time
from credentials import *


class AlertScript:
    def __init__(self):
        pass

    def get_board_by_id(self, id):
        url = "https://api.trello.com/1/boards/" + id + "/"
        querystring = {"actions": "all", "boardStars": "none", "cards": "none", "card_pluginData": "false",
                       "checklists": "none",
                       "customFields": "false",
                       "fields": "name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames",
                       "lists": "open", "members": "none", "memberships": "none", "membersInvited": "none",
                       "membersInvited_fields": "all", "pluginData": "false", "organization": "false",
                       "organization_pluginData": "false", "myPrefs": "false",
                       "tags": "false", "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
        response = requests.request("GET", url, params=querystring)

    def get_lists_on_a_board(self, board_id):
        url = "https://api.trello.com/1/boards/" + board_id + "/lists"
        querystring = {"key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
        response = requests.request("GET", url, params=querystring)

    def get_labels_on_a_board(self, board_id):
        url = "https://api.trello.com/1/boards/" + board_id + "/labels"
        querystring = {"key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
        response = requests.request("GET", url, params=querystring)

    def create_a_new_card(self, list_id, labels_id):
        url = "https://api.trello.com/1/cards"
        name = time.strftime("%Y%m%d") + "_" + time.strftime("%H%M%S") + "_" + "TEST_card"
        description = "TEST_description"
        position = "top"
        querystring = {"key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN, "name": name, "desc": description,
                   "pos": position, "idList": list_id, "idLabels": labels_id}
        response = requests.request("POST", url, params=querystring)

    def run_script(self):
        pass