"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from mysite.view import hello ,datetime,date_arrival,name,display_meta
from books import views
from django.conf.urls import include
admin.autodiscover()

urlpatterns = [
    url(r'^hello/',hello),
    url(r'^time/$',datetime),
    url(r'^arrival/plus/(\d{1,2})/$',date_arrival),
    url(r'^name/$',name),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^display/$',display_meta),
    url(r'^search/$',views.search),
    url(r'^search_form/$',views.search_form),
    url(r'^contact/$',views.contact),
    url(r'^contact/thanks/$',views.thanks),
    url(r'^shift/$',views.shift),
]
