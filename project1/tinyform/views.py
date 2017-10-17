# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from forms import tinyFormTest
from .models import tinytest
from django.shortcuts import render

# Index page view --
def home(request):
    form = tinyFormTest()
    context =  {
        'form' : form,
    }
    return render(request, 'form.html', context)
