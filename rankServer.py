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


import requests
import json

from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
from xml.etree import ElementTree


app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)


def get_alexa_xml(args):
    """
    Abstract function that pulls in xml data from url
    and returns that data.
    """
    response = requests.get('http://data.alexa.com/data?cli=10&url=http://' + args)
    tree = ElementTree.fromstring(response.text)
    return tree


@app.route('/domain_rank')
@payment.required(750)
def get_rank():
    """
    Input: Specific URL.
    Output: JSON-encoded Alexa rankings of URL.
    Exception raised if domain not found in rankings or does not rank high enough.
    """
    url = request.args.get('url')
    
    try:
        rank = get_alexa_xml(url).find(".//REACH").get("RANK")
        delta = get_alexa_xml(url).find(".//RANK").get("DELTA")
        params = {
            'domain-rank': {
                'rank': rank,
                'rank-change': delta,
                'url': url
            }
        }
        return json.dumps(params, indent=2)
    except:
        params = {'alexa-ranking': {'ranking': 'this domain is not ranked'}}
        return json.dumps(params, indent=2)

if __name__ == '__main__':
    app.run(host="::", port=7002)
