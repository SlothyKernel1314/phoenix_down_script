# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
from constants import *
import requests
import time


def get_board_by_id(id):
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
    print(response.text)


def get_open_cards_by_board_id(id):
    url = "https://api.trello.com/1/boards/" + id + "/lists"
    querystring = {"cards": "open", "card_fields": "all", "filter": "open", "fields": "all",
                   "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


def get_card_by_id(id):
    url = "https://api.trello.com/1/cards/" + id + ""
    querystring = {"attachments": "false", "attachment_fields": "all", "members": "false", "membersVoted": "false",
                   "checkItemStates": "false", "checklists": "none", "checklist_fields": "all", "board": "false",
                   "list": "false", "pluginData": "false", "stickers": "false", "sticker_fields": "all",
                   "customFieldItems": "false", "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


def get_boards_by_member_username(username):
    url = "https://api.trello.com/1/members/" + username + "/boards"
    querystring = {"filter": "all", "fields": "all", "lists": "none", "memberships": "none", "organization": "false",
                   "organization_fields": "name,displayName", "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


# def post_card():
#     url = "https://api.trello.com/1/cards"
#     name = time.strftime("%Y%m%d") + "_" + time.strftime("%H%M%S") + "_" + "TEST_card"
#     description = "TEST_description"
#     position = "top"
#     querystring = {"key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN, "name": name, "des": description,
#                    "pos": position, "idList": pass}
#     response = requests.request("POST", url, params=querystring)
#     print(response.text)

def get_list_on_a_board(board_id):
    url = "https://api.trello.com/1/boards/" + board_id + "/lists"
    querystring = {"key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
