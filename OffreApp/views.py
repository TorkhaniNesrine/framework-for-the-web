from django.views.generic import ListView
from .models import Offre
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import OffreForm

class CreateOffre(CreateView):
    model = Offre
    form_class = OffreForm
    template_name = 'offre/forms.html'  
    success_url = reverse_lazy('liste_offre_classe')

class UpdateOffre(UpdateView):
    model = Offre
    form_class = OffreForm  
    template_name = 'offre/forms.html' 
    success_url = reverse_lazy('liste_offre_classe')
class DeleteOffre(DeleteView):
    model = Offre
    template_name = 'offre/delete.html'
    success_url = reverse_lazy('liste_offre_classe') 
class Detail_offre(DetailView):
    model = Offre
    template_name = 'offre/detail.html'
    context_object_name = 'offre'
class Liste_offre(ListView):
    model = Offre
    template_name = 'offre/offre_list.html'  
    context_object_name = 'offres'                