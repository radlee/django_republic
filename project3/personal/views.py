# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from personal.models import User
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/index.html')

def create_user(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create(
        name = name,
        email = email,
        password = password
        )

        return HttpResponse('')
