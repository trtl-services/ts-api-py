# Copyright (c) 2018, Fexra, The TurtleCoin Developers
#
# Please see the included LICENSE file for more information.

from . import _get
from . import _post
from . import _delete
import json

class TS(object):

    def __init__(self, id):
        self.id = id
    
    # Create Address
    def createAddress():

        data = {}
        response = _post('address', data)
        return response


    # Get Address
    def getAddress(address):

        response = _get('address/' + address)
        return json.dumps(response)


    # Delete Address
    def deleteAddress(address):

        response = _delete('address/' + address)
        return json.dumps(response)


    # Get Addresses
    def getAddresses():

        response = _get('address/all')
        return json.dumps(response)


    # Scan Address
    def scanAddress(address, blockIndex):

        response = _get('address/scan/' + address + '/' + str(blockIndex))
        return response


    # Get Address Keys
    def scanAddress(address):

        response = _get('address/keys/' + address)
        return json.dumps(response)


    # Integrate Address
    def integrateAddress(from_address, to_address, amount, fee, paymentId=None, extra=None):

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

        response = _post('address/integrate', data)
        return json.dumps(response)


    # Get Integrated Addresses
    def getIntegratedAddresses(address):

        response = _get('address/integrate/' + address)
        return json.dumps(response)


    # Get Fee
    def getFee(amount):

        response = _get('transfer/fee/' + str(amount))
        return response


    # Create Transfer
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
        return response


    # Get Transfer
    def getTransfer(transactionHash):

        response = _get('transfer/' + transactionHash)
        return json.dumps(response)


    # Get Wallet
    def getStatus():

        response = _get('status')
        return json.dumps(response)


    # Get Status
    def getStatus():
        
        response = _get('status')
        return response
