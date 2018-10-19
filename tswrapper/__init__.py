# Copyright (c) 2018, Fexra, The TurtleCoin Developers
#
# Please see the included LICENSE file for more information.

import os
import requests
import json

BASE_URL = "https://api.trtl.services"
TOKEN = os.environ.get('TRTL_SERVICES_TOKEN', "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWxsIiwiYXBwSWQiOjIwLCJ1c2VySWQiOjIsInBlcm1pc3Npb25zIjpbImFkZHJlc3M6bmV3IiwiYWRkcmVzczp2aWV3IiwiYWRkcmVzczphbGwiLCJhZGRyZXNzOnNjYW4iLCJhZGRyZXNzOmRlbGV0ZSIsInRyYW5zZmVyOm5ldyIsInRyYW5zZmVyOnZpZXciXSwiaWF0IjoxNTM5OTQ4MzI1LCJleHAiOjE1NzE1MDU5MjUsImF1ZCI6ImdhbmcuY29tIiwiaXNzIjoiVFJUTCBTZXJ2aWNlcyIsImp0aSI6IjIwIn0.7SkanH5QPvP6PpeMNQLU_5dR6Lm2U73Cu7NRid6-xQTB7ueChTdX0FzoURxR3hi8daIk9Y_TE689CqauvfSauA")

if not TOKEN:
    raise Exception('All methods require an API key. See https://trtl.services/documentation')
    
def _get(method):
    response = requests.get(
        BASE_URL + '/' + method,
        headers = { 'Authorization': 'Bearer ' + TOKEN }
    ).json()

    return response
    
def _post(method, params):
    response = requests.post(
        BASE_URL + '/' + method,
        headers = { 'Authorization': 'Bearer ' + TOKEN },
        json = params
    ).json()
    
    return response

def _delete(method):
    response = requests.delete(
        BASE_URL + '/' + method,
        headers = { 'Authorization': 'Bearer ' + TOKEN },
    ).json()

    return response

from .lib import TRTLServices