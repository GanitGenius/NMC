# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=250)
    passwd = models.CharField(max_length=250)

class Schedule(models.Model):
    """
    Store schedule in 24-hr format.
    """
    day = models.CharField(max_length=3)
    hrs = models.CharField(max_length=2)
    mins = models.CharField(max_length=2)

class UserSchedule(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
