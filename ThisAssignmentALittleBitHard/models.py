# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class whatIWant(models.Model):
    car = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    def __str__(self):
        return "CAR: " + self.car + " INCOME: " + self.income + " MY WORK: " + self.work

class whatIHave(models.Model):
    my_colleague = models.CharField(max_length=100)
    what = models.ForeignKey(whatIWant, on_delete=models.CASCADE)
    def __str__(self):
        return self.my_colleague + " is my colleague"