from django import forms
from .models import Entreprise

class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['raison_social', 'matricule_fiscal', 'type_entreprise', 'adresse']