# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class persona(models.Model):
		Nombre = models.CharField(max_length=50)
		Apellido_Paterno = models.CharField(max_length=24)
		Apellido_Materno = models.CharField(max_length=24)
		Edad = models.IntegerField()

		def __unicode__(self):
			return self.Nombre
