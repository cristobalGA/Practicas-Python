# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class disquera(models.Model):
    iddisquera = models.CharField(max_length = 70)
    nombredisquera = models.CharField(max_length = 70, primary_key=True)
    nodiscos = models.IntegerField()
    ceo = models.CharField(max_length = 70)
    
    def __unicode__(self):
        return self.nombredisquera

class manager(models.Model):
    idmanager = models.CharField(max_length = 30)
    nombremanager = models.CharField(max_length = 30, primary_key=True)
    fechanacmanager = models.DateField()

    def __unicode__(self):
        return self.nombremanager


class musico(models.Model):
    idmusico = models.CharField(max_length = 70)
    nombremusico = models.CharField(max_length = 30, primary_key=True)
    fechanacmusico = models.DateField()
    nodiscosmusico = models.IntegerField()

    def __unicode__(self):
        return self.nombremusico


class disco(models.Model):
    iddisco = models.CharField(max_length = 30)
    nombredisco = models.CharField(max_length = 30, primary_key=True)
    nocanciones = models.IntegerField()
    artista = models.CharField(max_length = 30)
    ano = models.DateField()
    
    def __unicode__(self):
        return self.nombredisco

class cancion(models.Model):
    idcancion = models.CharField(max_length = 30)
    nombrecancion = models.CharField(max_length = 30, primary_key=True)
    anodisco = models.DateField()

    def __unicode__(self):
        return self.nombrecancion

