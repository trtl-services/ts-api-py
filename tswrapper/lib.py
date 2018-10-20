# Copyright (c) 2018, Fexra, The TurtleCoin Developers
#
# Please see the included LICENSE file for more information.

from . import _get
from . import _post
from . import _delete
import json

class TRTLServices(object):

    def __init__(self, id):
        self.id = id
        
    def createAddress():
        data = {}
        response = _post('address', data)
        return json.dumps(response)


    def deleteAddress(address):

        response = _delete('address/' + address)
        return json.dumps(response)


    def viewAddress(address):

        response = _get('address/view/' + address)
        return json.dumps(response)


    def viewAddresses():

        response = _get('address/view/all')
        return json.dumps(response)


    def scanAddress(address, blockIndex):

        response = _get('address/scan/' + address + '/' + str(blockIndex))
        return json.dumps(response)


    def getFee(amount):

        response = _get('transfer/fee/' + str(amount))
        return json.dumps(response)

    def createTransfer(from_address, to_address, amount, fee, paymentId=None, extra=None):

        if paymentId is None:
            paymentId = ''
            
        if extra is None:
            extra = ''

        data = {
            'from': from_address,
            'to': to_address,
            'amount': float(amount),
            'fee': float(fee),
            'paymentId': paymentId,
            'extra': extra
        }


        response = _post('transfer', data)
        return json.dumps(response)


    def viewTransfer(transactionHash):

        response = _get('transfer/view/' + transactionHash)
        return json.dumps(response)


    def getStatus():

        response = _get('status')
        return json.dumps(response)