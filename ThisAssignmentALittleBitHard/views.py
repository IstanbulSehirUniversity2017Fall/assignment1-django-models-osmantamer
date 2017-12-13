# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_details(request, mycar):
    return HttpResponse("<h2>%s is what i want.<h2>"%str(mycar))

def main_page(request):
    return HttpResponse("<img src='https://memegenerator.net/img/instances/500x/64716536/hey-buddy-how-ya-doin.jpg'><h2>You are in the wrong page.<h2>"
                        "<h2>type /ThisAssignmentALittleBitHard/(car_brand_here)/</h2>")