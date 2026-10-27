from django.shortcuts import render
from django.http import HttpResponse
from .models import Expedition
# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome to </h1>")#affichage message simple 
def welcome(request,name):
    return HttpResponse(f"Hello {name}")
def listExpeditions(request):
    liste = Expedition.objects.all()
    return render(request,'expedition/list.html',{"list":liste})
def detailsExpedition(request,id):
    expedition = Expedition.objects.get(id=id)
    return render(request, 'expedition/details.html',{"expedition":expedition})
