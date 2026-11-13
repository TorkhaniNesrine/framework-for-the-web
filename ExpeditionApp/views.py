from django.shortcuts import render
from django.http import HttpResponse
from .models import Expedition
from django.views.generic import ListView, DetailView, DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import ExpeditionForm  

def home(request):
    return HttpResponse("<h1> Welcome to </h1>")

def welcome(request, name):
    return HttpResponse(f"Hello {name}")

def listExpeditions(request):
    liste = Expedition.objects.all()
    # J'ai remplacé "list" par "expeditions" ici 👇
    return render(request, 'expedition/expedition_list.html', {"expeditions": liste})
# Cette fonction est utilisée par la route 'detail'
def detailsExpedition(request, id):
    expedition = Expedition.objects.get(id=id)
    return render(request, 'expedition/detail.html', {"expedition": expedition})

class Liste_expedition(ListView):
    model = Expedition
    template_name = 'expedition/expedition_list.html'  
    context_object_name = 'expeditions'                

class Detail_expedition(DetailView):
    model = Expedition
    template_name = 'expedition/detail.html'
    context_object_name = 'expedition'
    
class DeleteExpedition(DeleteView):
    model = Expedition
    template_name = 'expedition/delete.html'
    success_url = reverse_lazy('liste_classe')
     
class CreateExpedition(CreateView):
    model = Expedition
    form_class = ExpeditionForm
    template_name = 'expedition/forms.html'  
    success_url = reverse_lazy('liste_classe')
class UpdateExpedition(UpdateView):
    model = Expedition
    form_class = ExpeditionForm  
    template_name = 'expedition/forms.html' 
    success_url = reverse_lazy('liste_classe')
    