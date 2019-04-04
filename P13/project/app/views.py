# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import *
from app.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView

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

def logeado(request):
    return render(request, 'logueado.html', {})

class persona(ListView):
    model = persona
    pk_url_kwarg = 'nombrepersona'
    template_name = 'persona.html'

class trabajo(ListView):
    model = trabajo
    pk_url_kwarg = 'nombretrabajo'
    template_name = 'trabajo.html'

class carro(ListView):
    model = carro
    pk_url_kwarg = 'nombrecarro'
    template_name = 'carro.html'

class pasatiempo(ListView):
    model = pasatiempo
    pk_url_kwarg = 'nombrepasatiempo'
    template_name = 'pasatiempo.html'

class comida(ListView):
    model = comida
    pk_url_kwarg = 'nombrecomida'
    template_name = 'comida.html'
    