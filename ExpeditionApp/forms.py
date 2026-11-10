from django import forms
from .models import Expedition

class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        exclude = ["id", "reference", "created_at", "updated_at"]   
