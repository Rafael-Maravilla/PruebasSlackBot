import re
from django.template import Context, Template, loader
from django.shortcuts import render

def vistaP(request):
    return render(request, "base.html")

def mivista(request):
    return render(request, "mivista.html")