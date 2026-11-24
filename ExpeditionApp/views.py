
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Expedition
from .forms import ExpeditionForm, RegisterUserForm


def home(request):
    return HttpResponse("<h1>Welcome to</h1>")


def welcome(request, name):
    return HttpResponse(f"Hello {name}")


def listExpeditions(request):
    liste = Expedition.objects.all()
    return render(request, 'expedition/expedition_list.html', {
        "expeditions": liste
    })


def detailsExpedition(request, id):
    expedition = Expedition.objects.get(id=id)
    return render(request, 'expedition/detail.html', {
        "expedition": expedition
    })


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request, 'expedition/register.html', {
        'form': form
    })


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
