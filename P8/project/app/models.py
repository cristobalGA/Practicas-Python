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
class carro(models.Model):
		Nombre_carro = models.CharField(max_length=50)
		Modelo = models.CharField(max_length=24)
		Costo = models.IntegerField()

		def __unicode__(self):
			return self.Nombre_carro

class trabajo(models.Model):
		Nombre_trabajo = models.CharField(max_length=50)
		Tipo_trabajo = models.CharField(max_length=24)
		Salario = models.IntegerField()

		def __unicode__(self):
			return self.Nombre_trabajo

class pasatiempo(models.Model):
		Nombre_pasatiempo = models.CharField(max_length=50)
		Tiempo = models.IntegerField()

		def __unicode__(self):
			return self.Nombre_pasatiempo

class comida(models.Model):
		Nombre_comida = models.CharField(max_length=50)
		Tipo_de_comida = models.CharField(max_length=24)

		def __unicode__(self):
			return self.Nombre_comida

