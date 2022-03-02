from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<a href='#'>Hello, world. You're at the polls index.</a>")
# Create your views here.
