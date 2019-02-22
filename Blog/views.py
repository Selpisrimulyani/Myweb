# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Artikel

# Create your views here.
def index(request):
    return render(request, 'Layout/index.html')
def about(request):
    return render(request, 'Layout/about.html')
def contact(request):
    return render(request, 'Layout/contact.html')
def blog(request):
    blogs = Artikel.objects.all()
    return render(request, 'Layout/blog.html',{'blogs':blogs})
