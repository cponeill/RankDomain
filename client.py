"""
Copyright (c) 2016-2017 Blockshare Technologies, LLC.
  ____  _            _     ____  _                      ___ ___  
 | __ )| | ___   ___| | __/ ___|| |__   __ _ _ __ ___  |_ _/ _ \ 
 |  _ \| |/ _ \ / __| |/ /\___ \| '_ \ / _` | '__/ _ \  | | | | |
 | |_) | | (_) | (__|   <  ___) | | | | (_| | | |  __/_ | | |_| |
 |____/|_|\___/ \___|_|\_\|____/|_| |_|\__,_|_|  \___(_)___\___/ 
"""

__author__ = "cponeill"
__version__ = "1.0"
__maintainer__ = "cponeill"
__email__ = "cponeill@blockshare.io"


import json

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests


wallet = Wallet()
requests = BitTransferRequests(wallet)

server_url = 'http://[fcce:a977:eee3:6ebf:1f21:0000:0000:0001]:7002/'

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
