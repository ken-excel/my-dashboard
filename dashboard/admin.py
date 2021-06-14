from django.contrib import admin

from .models import Computer, Temperature, Fan

admin.site.register(Computer)
admin.site.register(Temperature)
admin.site.register(Fan)