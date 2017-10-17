# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
