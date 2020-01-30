from utilities import *
from credentials import *
import requests


def get_boards_id_by_member_username(username):
    url = "https://api.trello.com/1/members/" + username + "/boards"
    querystring = {"filter": "all", "fields": "all", "lists": "none", "memberships": "none",
                   "organization": "false", "organization_fields": "name,displayName",
                   "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    datas = response.json()
    shortlinks_with_name_boards = []
    for board in datas:
        # we get shortlinks instead ids just because the API allows this + more simple
        shortlink_board = board['shortLink']
        shortlinks_with_name_boards.append(shortlink_board)
    return shortlinks_with_name_boards


def trello_script():
    # If the work directory "../trello" doesn't existe yet...
    # ... creation of this directory
    create_directory(PD_SCRIPT_TRELLO_DIRECTORY_PATH)
    get_boards_id_by_member_username(PD_SCRIPT_TRELLO_MEMBER_USERNAME)


