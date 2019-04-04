"""P5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .views import *


urlpatterns = [
    url(r'^$', views.vistadefault, name='vistadefault'),
    url(r'^vistauno/$', views.vistauno, name='vistauno'),
    url(r'^vistados/$', views.vistados, name='vistados'),
    url(r'^vistatres/$', views.vistatres, name='vistatres'),
    url(r'^vistacuatro/$', views.vistacuatro, name='vistacuatro'),
    url(r'^vistacinco/$', views.vistacinco, name='vistacinco'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^accounts/profile/$', views.logeado, name='logeado'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url('^signup/', CreateView.as_view(
            template_name='signup.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    #url detailview
    url(r'^manager/(?P<nombremanager>[-\w]+)/$', managerDetail.as_view(), name='detail'),
    url(r'^disquera/(?P<nombredisquera>[-\w]+)/$', disqueraDetail.as_view(), name='detail'),
    url(r'^disco/(?P<nombredisco>[-\w]+)/$', discoDetail.as_view(), name='detail'),
    url(r'^musico/(?P<nombremusico>[-\w]+)/$', musicoDetail.as_view(), name='detail'),
    url(r'^cancion/(?P<nombrecancion>[-\w]+)/$', cancionDetail.as_view(), name='detail'),

    #Updateview
    url(r'^discoupdate/(?P<nombredisco>[-\w]+)/$',discoupdate.as_view(),name='discoupdate'),
    url(r'^musicoupdate/(?P<nombremusico>[-\w]+)/$',musicoupdate.as_view(),name='musicoupdate'),
    url(r'^cancionupdate/(?P<nombrecancion>[-\w]+)/$',cancionupdate.as_view(),name='cancionupdate'),
    url(r'^managerupdate/(?P<nombremanager>[-\w]+)/$',managerupdate.as_view(),name='managerupdate'),
    url(r'^disqueraupdate/(?P<nombredisquera>[-\w]+)/$',disqueraupdate.as_view(),name='disqueraupdate'),
]
