from django import forms
from .models import Vehicule

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['immatricule', 'capacite_kg', 'disponible', 'type_vehicule', 'entreprise']