from django.views.generic import ListView
from .models import Entreprise
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import EntrepriseForm

class CreateEntreprise(CreateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = 'entreprise/forms.html'  
    success_url = reverse_lazy('liste_entreprise_classe')

class UpdateEntreprise(UpdateView):
    model = Entreprise
    form_class = EntrepriseForm  
    template_name = 'entreprise/forms.html' 
    success_url = reverse_lazy('liste_entreprise_classe')
class DeleteEntreprise(DeleteView):
    model = Entreprise
    template_name = 'entreprise/delete.html'
    success_url = reverse_lazy('liste_entreprise_classe') 
class Detail_entreprise(DetailView):
    model = Entreprise
    template_name = 'entreprise/detail.html'
    context_object_name = 'entreprise'
class Liste_entreprise(ListView):
    model = Entreprise
    template_name = 'entreprise/entreprise_list.html'  
    context_object_name = 'entreprises'                