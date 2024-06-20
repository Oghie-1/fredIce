from django.shortcuts import render
from django.http import HttpResponse
from django.views import View, generic


# Create your views here.

def homepage(request):
    return render(request, 'fredapp/base.html')