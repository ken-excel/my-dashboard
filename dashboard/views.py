from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Computer, Crypto, Spotify

import os
import urllib.request
import json
import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date, timedelta

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
        
class SpotifyView(generic.ListView):
    template_name = 'dashboard/spotify.html'
    context_object_name = 'artists_list'

    current_date = date.today().isoformat()   
    days_before = (date.today()-timedelta(days=30)).isoformat()

    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_KEY')

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                            client_secret=client_secret))

    def get_queryset(self):
        artists = []
        for artist_obj in Spotify.objects.all():
            artist={}
            artist['name'] = artist_obj.name
            artist['albums'] = []
            results = self.sp.artist_albums(artist_obj.uri, limit=50)
            albums = results['items']
            while results['next']:
                results = self.sp.next(results)
                albums.extend(results['items'])

            for album in albums:
                if album['release_date'] > self.days_before:
                    artist['albums'].append(album)

            artists.append(artist)
        
        return artists
        