from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Computer, Crypto

import os
import urllib.request
import json
import logging

class PCMonitorView(generic.ListView):
    template_name = 'dashboard/pcmonitor.html'
    context_object_name = 'computer_list'
    
    def get_queryset(self):
        return Computer.objects.order_by('type')

class CryptoView(generic.ListView):
    template_name = 'dashboard/crypto.html'
    context_object_name = 'crypto_list'

    def get_queryset(self):
        symbol_list = []
        for crypto_obj in Crypto.objects.all():
            symbol_list.append(crypto_obj.name)
        symbols = ','.join(symbol_list)
        api_key = os.environ.get('LUNARCRUSH_API_KEY')
        url = "https://api.lunarcrush.com/v2?data=assets&key=" + api_key + "&symbol=" + symbols
        assets = json.loads(urllib.request.urlopen(url).read())
        logging.debug(assets['data'])
        return assets['data']
        