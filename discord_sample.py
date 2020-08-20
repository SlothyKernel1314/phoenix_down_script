import base64
import requests
from credentials import *

API_ENDPOINT = 'https://discord.com/api/v6'
CLIENT_ID = DISCORD_CLIENT_ID
CLIENT_SECRET = DISCORD_CLIENT_SECRET


def get_token():
    data = {
        'grant_type': 'client_credentials',
        'scope': 'identify connections'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post('%s/oauth2/token' % API_ENDPOINT,
                             data=data,
                             headers=headers,
                             auth=(CLIENT_ID, CLIENT_SECRET))
    datas = response.json()
    print(datas)
    return datas


# def get_current_user():
#     data = {
#         'grant_type': 'client_credentials',
#         'scope': 'identify connections'
#     }
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     response = requests.post('%s/oauth2/token' % API_ENDPOINT,
#                              data=data,
#                              headers=headers,
#                              auth=(CLIENT_ID, CLIENT_SECRET))
#     datas = response.json
#     print(datas)
#     return datas
