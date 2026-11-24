
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Expedition

User = get_user_model()



class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        exclude = ["id", "reference", "created_at", "updated_at"]



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
