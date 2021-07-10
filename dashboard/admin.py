from django.contrib import admin

from .models import Computer, Temperature, Fan, Crypto, Spotify

admin.site.register(Computer)
admin.site.register(Temperature)
admin.site.register(Fan)
admin.site.register(Crypto)
admin.site.register(Spotify)