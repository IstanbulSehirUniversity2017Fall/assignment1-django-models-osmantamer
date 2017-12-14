# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_details(request, mycar):
    return HttpResponse("<h2>%s is what i want.<h2>"%str(mycar))

def main_page(request):
    return HttpResponse("<img src='https://i.ytimg.com/vi/5qfzqNtfP_Q/hqdefault.jpg'><h2>You are in the wrong page.<h2>"
                        "<h2>type /ThisAssignmentALittleBitHard/(car_brand_here)/</h2>")
