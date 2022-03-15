from django.shortcuts import render
from django.http import HttpResponse

def signup(request):
    email=request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html',
{'searchTerm':searchTerm}) 



def index(request):
    return HttpResponse("<style> *{background:white;} nav{color:black;}</style><a href='#'>Hello, Colombia . You're at the polls index.</a>")
# Create your views here.
