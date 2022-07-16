# encoding: utf-8
"""
@author: wbytts
@desc: 
"""
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")
