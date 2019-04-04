# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(persona)
admin.site.register(carro)
admin.site.register(trabajo)
admin.site.register(pasatiempo)
admin.site.register(comida)