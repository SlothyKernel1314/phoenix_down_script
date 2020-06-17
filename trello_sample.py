# -*- coding: utf-8 -*-
# !/usr/bin/env python

from credentials import *
import requests


def get_board_by_id_sample_version(id):
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


def get_open_cards_by_board_id_sample_version(id):
    url = "https://api.trello.com/1/boards/" + id + "/lists"
    querystring = {"cards": "open", "card_fields": "all", "filter": "open", "fields": "all",
                   "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


def get_card_by_id_sample_version(id):
    url = "https://api.trello.com/1/cards/" + id + ""
    querystring = {"attachments": "false", "attachment_fields": "all", "members": "false", "membersVoted": "false",
                   "checkItemStates": "false", "checklists": "none", "checklist_fields": "all", "board": "false",
                   "list": "false", "pluginData": "false", "stickers": "false", "sticker_fields": "all",
                   "customFieldItems": "false", "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


def get_boards_by_member_username_sample_version(username):
    url = "https://api.trello.com/1/members/" + username + "/boards"
    querystring = {"filter": "all", "fields": "all", "lists": "none", "memberships": "none", "organization": "false",
                   "organization_fields": "name,displayName", "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
