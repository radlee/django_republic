# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    context = {
        'name' : 'Lolito'
    }
    return render(request, 'personal/home.html', context)

def tracks(request):
    context = {'content': ["Da La Soul - The Grind Date", "Ruff Ryders - Knock Knock", "Bump J - Move Around", "Grafh - I don't Care"]}
    return render(request, 'personal/basic.html', context)
