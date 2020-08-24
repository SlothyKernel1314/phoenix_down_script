# -*- coding: utf-8 -*-
# !/usr/bin/env python

import requests
import time
from credentials import *
from constants import *
from utilities import *


class AlertScript:
    def __init__(self):
        self.logger_sub_path = "/logger"

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

    def create_a_new_card_with_alert_message(self, list_id, labels_id, alert_message):
        url = "https://api.trello.com/1/cards"
        name = time.strftime("%Y%m%d") + "_" + time.strftime("%H%M%S") + "_" + "Phoenix_Down_Script_ALERT"
        position = "top"
        querystring = {"key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN, "name": name, "desc": alert_message,
                       "pos": position, "idList": list_id, "idLabels": labels_id}
        response = requests.request("POST", url, params=querystring)

    def parse_logger_file_and_create_alert_mail_message(self, logger_file_to_parse):
        warnings_count = 0
        errors_count = 0
        # opens the file for reading only
        file = open(logger_file_to_parse, "r")
        for line in file.readlines():
            print(line)
            if "[WARNING]" in line:
                warnings_count += 1
            if "[ERROR]" in line:
                errors_count += 1
        file.close()
        alert_mail_message = "During the last execution of Phoenix Down Script, " \
                             "the logger returned " + str(warnings_count) + \
                             " warning messages, and " \
                             + str(errors_count) + " error messages. " \
                                                   "Please check that the script is working properly !"
        return alert_mail_message, warnings_count, errors_count

    def run_script(self):
        logger_file_to_parse = get_the_latest_file_in_a_folder(PD_SCRIPT_ROOT_LOGS_PATH + self.logger_sub_path)

        callback_alert_infos = self.parse_logger_file_and_create_alert_mail_message(logger_file_to_parse)

        if callback_alert_infos[1] > 0 or callback_alert_infos[2] > 0:
            self.create_a_new_card_with_alert_message(TRELLO_ALERT_BOARD_ALERT_LIST_ID,
                                                      TRELLO_ALERT_URGENT_CUSTOM_LABEL_ID, callback_alert_infos[0])
            self.create_a_new_card_with_alert_message(TRELLO_MBL_BOARD_ADMIN_LIST_ID,
                                                      TRELLO_MBL_URGENT_CUSTOM_LABEL_ID, callback_alert_infos[0])
