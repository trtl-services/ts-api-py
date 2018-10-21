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
        """
        Creates an address and return information on it

        Returns:
            dict:

            {
	            'address': 'TRTLv37JQX6J1zkPuX4emFauwkEwBzTXUZzg2fLJMGyNPrtow313wP69tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7fYZQjr',
	            'blockIndex': 902727
            }
        """
        data = {}
        response = _post('address', data)
        return response


    def deleteAddress(address):
        """
        Deletes given address

        Args:
            address (str): A valid, registered address associated with your account.

        Returns:
            dict:

            {

            }

        """

        response = _delete('address/' + address)
        return response


    def viewAddress(address):
        """
        Returns balance of given address

        Args:
            address (str): A valid, registrated address associated with your account.
        
        Returns:
            dict:

            {
                'balance': 100, 
                'locked': 1, 
                'blockIndex': 902727
            }
        
        """

        response = _get('address/view/' + address)
        return response


    def viewAddresses():
        """
        Returns array of addresses registered with your account

        Returns:
            array:

            ['TRTLuzNvqUjFJSs6dLy64jbpZTegTn4Kifoz1JRsrnG3X3E7UmFHuWg9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7b99q43', 'TRTL...']
        
        """

        response = _get('address/view/all')
        return response


    def scanAddress(address, blockIndex):
        """
        Scans for transactions in the next 100 blocks from the specified block height for the specified address.

        Args:
            address (str): A valid, registrated address associated with your account
            blockIndex (int): Block height to scan for transactions from

        Response:
            [{
                'address': 'TRTLuwhPmz2VdjUH58K7dL4YiWvr6P5tvJaPPrdW11MLAMudy7QRbqJ9tK92j9kurSKdXVHFmjSRkaNBxM6Nb3G8eQGL7fPfnZs',
                'amount': 10,
                'fee': 0.1,
                'sfee': 0,
                'transactionHash': 'abbd3f9762112a24b7cfb15423525f92c0f26809913c980142fbd9e32d5fb118',
                'blockHash': 'a33d24714df6be2cf7c2ac8ebf934813e6da14756834ad70a08ee9b0bfd241ed',
                'paymentId': 'ac8889dfb7c93471a9a43c287f3fa40854b64454e62eb0006b13e510e6ad8a8e',
                'timestamp': 1540142870,
                'blockIndex': 904897,
                'confirms': 41
            }]      
        """


        response = _get('address/scan/' + address + '/' + str(blockIndex))
        return response


    def getFee(amount):
        """
        Calculate the TRTL Services fee for a specified TRTL amount.

        Args:
            amount (int): Transaction amount to calculate fee for

        Response:
            dict:

            {
                'sfee': 21
            }
        """

        response = _get('transfer/fee/' + str(amount))
        return response

    def createTransfer(from_address, to_address, amount, fee, paymentId=None, extra=None):
        """
        Send a TRTL transaction with a specified account.

        Args:
            ---
            Required
            ---
            from_address (str): TRTL address to send tx from(must be registered with TRTL.services)
            to_address (str): TRTL address to send tx to (doesn't need to be registered)
            amount (int): Amount of TRTL to sned
            fee(int): Fee to include with the transaction (in turtles). Minimum is 0.10 TRTL.
            *Note that TRTL.services fee of 2.1% will be added on top of the selected fee*

            ---
            Optional
            ---
            paymentId (str): Payment ID to include with the transaction
            extra (str): Data to include in the tx_extra field of the transaction

        Response:
            {
                'transactionHash': 'e25dfb42f1723eac03bc7dc656d402f8beb42471cda4389db52c5aadc07b5908'
            }
        """

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


    def viewTransfer(transactionHash):
        """
        Lists transaction details with specified hash.

        Args:
            transactionHash (str): valid transaction hash to check details of
            
        Response:
            {
                'address': 'TRTLv3pFrFm2yk4cYNtKf5fxV1b594tNrZfEV2CYWJsTSqr9BWoWMrUNpQaeD9StrzQrxpRQKPCdd1FfvT6D6dAg4pY6iB7sqsG',
                'amount': 5,
                'fee': 1,
                'sfee': 0.11,
                'transactionHash': 'e25dfb42f1723eac03bc7dc656d402f8beb42471cda4389db52c5aadc07b5908',
                'blockHash': None,
                'paymentId': '',
                'timestamp': None,
                'blockIndex': 905125,
                'confirms': 2
            }

        """

        response = _get('transfer/view/' + transactionHash)
        return response


    def getStatus():
        """
        Returns status of TRTL.services

        Response:
            dict:

            [{
                'name': 'chain',
                'state': 1,
                'status': 'OK',
                'synced': 1,
                'blockIndex': 902727,
                'timestamp': '2018-10-21'
            }, {
                'name': 'wallet',
                'state': 1,
                'status': 'Synced',
                'synced': 1,
                'blockIndex': 902727,
                'timestamp': '2018-10-21'
            }, {
                'name': 'worker',
                'state': 1,
                'status': 'Online',
                'synced': 0,
                'blockIndex': 0,
                'timestamp': '2018-10-21'
            }, {
                'name': 'api',
                'state': 1,
                'status': 'Online',
                'synced': 1,
                'blockIndex': 0,
                'timestamp': '2018-10-21'
            }]

        """

        response = _get('status')
        return response
