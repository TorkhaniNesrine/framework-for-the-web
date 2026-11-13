from django.views.generic import ListView
from .models import Vehicule
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import VehiculeForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Vehicule
from .forms import VehiculeForm


class Liste_vehicule(ListView):
    model = Vehicule
    template_name = 'vehicule/vehicule_list.html'  
    context_object_name = 'vehicules'    
class Detail_vehicule(DetailView):
    model = Vehicule
    template_name = 'vehicule/detail.html'
    context_object_name = 'vehicule'
class DeleteVehicule(DeleteView):
    model = Vehicule
    template_name = 'vehicule/delete.html'
    success_url = reverse_lazy('vehicule:liste_vehicule_classe')
class CreateVehicule(CreateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = 'vehicule/forms.html'  
    success_url = reverse_lazy('vehicule:liste_vehicule_classe')

class UpdateVehicule(UpdateView):
    model = Vehicule
    form_class = VehiculeForm  
    template_name = 'vehicule/forms.html' 
    success_url = reverse_lazy('vehicule:liste_vehicule_classe')
            