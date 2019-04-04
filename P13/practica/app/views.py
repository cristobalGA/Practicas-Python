# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import *
from app.forms import disqueraForm, musicoForm, discoForm, cancionForm, managerForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView

# Create your views here.
def vistadefault(request):
    return render(request, 'default.html', {})

def logeado(request):
    return render(request, 'logeado.html', {})

def vistauno(request):
    form = disqueraForm()
    return render(request, 'vista1.html', {'form': form})

def vistados(request):
    form = musicoForm()
    return render(request, 'vista2.html', {'form': form})

def vistatres(request):
    form = discoForm()
    return render(request, 'vista3.html', {'form': form})

def vistacuatro(request):
    form = cancionForm()
    return render(request, 'vista4.html', {'form': form})

def vistacinco(request):
    form = managerForm()
    return render(request, 'vista5.html', {'form': form})


#DetailViews
class managerDetail(DetailView):
    model = manager
    pk_url_kwarg = 'nombremanager'
    template_name = "detailmanager.html"

class disqueraDetail(DetailView):
    model = disquera
    pk_url_kwarg = 'nombredisquera'
    template_name = "detaildisquera.html"

class discoDetail(DetailView):
    model = disco
    pk_url_kwarg = 'nombredisco'
    template_name = "detaildisco.html"

class cancionDetail(DetailView):
    model = cancion
    pk_url_kwarg = 'nombrecancion'
    template_name = "detailcancion.html"

class musicoDetail(DetailView):
    model = musico
    pk_url_kwarg = 'nombremusico'
    template_name = "detailmusico.html"

