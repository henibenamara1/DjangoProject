from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader



def index(request):
    
    return render(request,'index.html')

def acc(request):
    
    return render(request,'accueil.html')
