"""project URL Configuration

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
from django.contrib import admin
from app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Index, name='index'),
    url(r'^v1/$', views.v1, name='v1'),
    url(r'^v2/$', views.v2, name='v2'),
    url(r'^v3/$', views.v3, name='v3'),
    url(r'^v4/$', views.v4, name='v4'),
    url(r'^v5/$', views.v5, name='v5'),
    
]
