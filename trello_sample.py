from credentials import *
import requests


def get_board_by_id():
    url = "https://api.trello.com/1/boards/"+TRELLO_MBL_BOARD_ID+"/"
    querystring = {"actions":"all","boardStars":"none","cards":"none","card_pluginData":"false","checklists":"none","customFields":"false","fields":"name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames","lists":"open","members":"none","memberships":"none","membersInvited":"none","membersInvited_fields":"all","pluginData":"false","organization":"false","organization_pluginData":"false","myPrefs":"false","tags":"false","key":TRELLO_API_KEY,"token":TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)

def get_open_cards_by_board_id():
    url = "https://api.trello.com/1/boards/"+TRELLO_MBL_BOARD_ID+"/lists"
    querystring = {"cards":"open","card_fields":"all","filter":"open","fields":"all","key":TRELLO_API_KEY,"token":TRELLO_SERVER_TOKEN}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
