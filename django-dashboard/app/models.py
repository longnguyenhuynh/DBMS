# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from typing import cast
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from authentication import models as aut

# Create your models here.

# Save information of transfer money from 2 account
class tranfer(models.Model):
    sender = models.ForeignKey(aut.user, on_delete=CASCADE, related_name="sender")
    receiver = models.ForeignKey(aut.user, on_delete=CASCADE, related_name="receiver")

    amount = models.IntegerField()
    note = models.TextField()
    time = models.DateTimeField()

# Save information of draw or deposit money 
class change_balanced(models.Model):
    account = models.ForeignKey(aut.user, on_delete=CASCADE, related_name="account")
    staff = models.ForeignKey(aut.user, on_delete=CASCADE, related_name="staff_take_money") # customer will draw or deposit with staff, not online

    amount = models.IntegerField()
    note = models.TextField()
    time = models.DateTimeField()







