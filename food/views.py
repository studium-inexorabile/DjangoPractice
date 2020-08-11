from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello World</h1>')

def item(request):
    return HttpResponse('<h2>This is an item view</h2>')