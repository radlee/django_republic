# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todo(model.Model):
    title = model.CharField(max_length=200)
    text = model.TextField()
    created_at = model.DateTimeField()
