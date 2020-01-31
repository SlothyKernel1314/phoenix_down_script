from utilities import *
from credentials import *
from constants import *
import requests

# VARIABLES ------------------------------------------------------------------------------------------------------------

application_name = "trello"


# FUNCTIONS ------------------------------------------------------------------------------------------------------------

def get_boards_shortlinks_as_keys_with_values(username):
    url = "https://api.trello.com/1/members/" + username + "/boards"
    querystring = {"filter": "all", "fields": "all", "lists": "none", "memberships": "none",
                   "organization": "false", "organization_fields": "name,displayName",
                   "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    datas = response.json()
    shortlinks_as_keys_with_values = {}
    for board in datas:
        # we get shortlinks instead ids just because the API allows this + more simple
        shortlink_board = board['shortLink']
        name_board = board['name']
        shortlinks_as_keys_with_values[shortlink_board] = [name_board]
    print(shortlinks_as_keys_with_values)
    return shortlinks_as_keys_with_values


def get_open_cards_by_board_id(id):
    url = "https://api.trello.com/1/boards/" + id + "/lists"
    querystring = {"cards": "open", "card_fields": "all", "filter": "open", "fields": "all",
                   "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    datas = response.json()
    return datas


def get_card_by_id(id):
    url = "https://api.trello.com/1/cards/" + id + ""
    querystring = {"attachments": "false", "attachment_fields": "all", "members": "false", "membersVoted": "false",
                   "checkItemStates": "false", "checklists": "none", "checklist_fields": "all", "board": "false",
                   "list": "false", "pluginData": "false", "stickers": "false", "sticker_fields": "all",
                   "customFieldItems": "false", "key": TRELLO_API_KEY, "token": TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    datas = response.json()
    return datas


# VARIABLES ------------------------------------------------------------------------------------------------------------

def trello_script():
    # If the work directory "../trello" doesn't existe yet...
    # ... creation of this directory
    create_directory(PD_SCRIPT_TRELLO_DIRECTORY_PATH)

    # get dictionnary with all shortlinks boards as keys, with values (name board)
    shortlinks_as_keys_with_values = get_boards_shortlinks_as_keys_with_values(PD_SCRIPT_TRELLO_MEMBER_USERNAME)

    # creation of name for log file
    file_name = create_timestamped_and_named_file(application_name)

    # creation of file with its name
    file = open(file_name, "w", encoding="utf-8")

    # writing in log file
    # processing of boards
    for shortlink in shortlinks_as_keys_with_values:
        name_board = shortlinks_as_keys_with_values[shortlink]
        file.write("##### JSON datas of " + str(name_board) + " board : \n\n")
        datas = get_open_cards_by_board_id(shortlink)
        file.write(str(datas))
        file.write("\n\n\n\n")
    # processing of particulary valuable cards
    for card in PD_SCRIPT_TRELLO_CARDS_IDS:
        datas = get_card_by_id(card)
        name_card = datas['name']
        file.write("##### JSON datas of " + str(name_card) + " valuable card : \n\n")
        file.write(str(datas))
        file.write("\n\n\n\n")



