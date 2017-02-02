#! /usr/bin/env python3
import json

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests


wallet = Wallet()
requests = BitTransferRequests(wallet)
server_url = 'http://[::]:7002/'


def get_rank():
    """Return JSON-encoded output of Alexa ranking for
       a specific domain url.
    """
    url = input()
    sel_url = server_url+'domain_rank?url={0}'
    response = requests.get(url=sel_url.format(url))
    print(response)


if __name__ == '__main__':
    get_rank()
