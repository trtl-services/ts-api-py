# Copyright (c) 2018, Fexra, The TurtleCoin Developers
#
# Please see the included LICENSE file for more information.

import os
import requests
import json

BASE_URL = "https://api.trtl.services"
TOKEN = os.environ.get('TRTL_SERVICES_TOKEN', None)

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