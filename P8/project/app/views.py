# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import *
from app.forms import *

# Create your views here.
def Index(request):
    return render(request, 'formaheredada.html', {})

def v1(request):
    form = personaForm()
    return render(request, 'v1.html', {'form': form})

def v2(request):
    form = carroForm()
    return render(request, 'v2.html', {'form': form})

def v3(request):
    form = trabajoForm()
    return render(request, 'v3.html', {'form': form})

def v4(request):
    form = pasatiempoForm()
    return render(request, 'v4.html', {'form': form})

def v5(request):
    form = comidaForm()
    return render(request, 'v5.html', {'form': form})