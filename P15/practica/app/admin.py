# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


#Mostrar datos en forma de lista y filtrarlos
class discoAdmin(admin.ModelAdmin):
    list_display = ('nombredisco', 'artista', 'nocanciones', 'ano')
    list_filter = ('nombredisco', 'artista')

class disqueraAdmin(admin.ModelAdmin):
    list_display = ('nombredisquera', 'nodiscos', 'ceo')
    list_filter = ('nombredisquera', 'nodiscos', 'ceo')

class managerAdmin(admin.ModelAdmin):
    list_display = ('nombremanager', 'fechanacmanager')
    list_filter = ('nombremanager', 'fechanacmanager')

class musicoAdmin(admin.ModelAdmin):
    list_display = ('nombremusico', 'fechanacmusico', 'nodiscosmusico')
    list_filter = ('nombremusico', 'fechanacmusico', 'nodiscosmusico')

class cancionAdmin(admin.ModelAdmin):
    list_display = ('nombrecancion', 'anodisco')
    list_filter = ('nombrecancion', 'anodisco')


#Registros
admin.site.register(disco, discoAdmin)
admin.site.register(disquera, disqueraAdmin)
admin.site.register(manager, managerAdmin)
admin.site.register(musico, musicoAdmin)
admin.site.register(cancion, cancionAdmin)
