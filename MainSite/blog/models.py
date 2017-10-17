# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create a Table called Post --
class Post(models.Model):
    #Collumns --
    title = models.CharField(max_length=140)
    authour = models.CharField(max_length=140)
    genre = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    # Reference string values of above atributes
    def __str__(self):
        return self.title
