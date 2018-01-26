#!/usr/bin/python2.7
from django.http import HttpResponse,Http404
import datetime
from datetime import datetime
from datetime import timedelta
import time 
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response


import pymongo
from pymongo import MongoClient

def hello(request):  
    connection = MongoClient('localhost', 27017)
    db = connection.video

# handle to names collection
    title = db.movies

    item = title.find_one()

    
    return HttpResponse ("hello wenting!\nI am ur server with mongDB!:)   "+
			"   This movie in sq is " +item["title"])

def datetime(request ):
    time_key = time.asctime(time.localtime(time.time()))
    return render_to_response('time.html',locals)
def date_arrival(request,offset):
    try :
       offset =  int(offset)
    except ValueError:
        raise Http404()
    offset_key = offset
    t = time.time()+int(offset)*10000000
    time_arrival=time.asctime(time.localtime(t))

    return render_to_response('time_arrive.html',locals())
def name(request):
   name_key = 'wenting'
   return render_to_response('name.html',locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for v in values:
         html.append(str(v))
    return render_to_response('get_meta.html',locals())
