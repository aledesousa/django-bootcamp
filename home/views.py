# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

'''
Get Bitcoin Value
http://api.coindesk.com/v1/bpi/currentprice.json
'''

import json
import urllib2

def get_btc():
    response = urllib2.urlopen('https://www.mercadobitcoin.net/api/BTC/ticker/')
    json_str = response.read()
    btc_data = json.loads(json_str)
    return btc_data['ticker']

btc_ticker = get_btc()
valor = ("R$ %.2f" % round(float(btc_ticker['last']),2))

def home(request):

    return render(request, 'home/home.html', {'title':'Preço do Bitcoin','price':valor})
