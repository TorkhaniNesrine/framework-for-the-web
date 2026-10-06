from django.db import models
from django.core.validators import MinValueValidator

class Vehicule(models.Model):
    immatriculation=models.CharField(max_length=200,unique=True)
    type_vehicule =models.CharField(choices=[('f','electrique'),('t','hybride')],default='f')
    capacite_kg=models.PositiveIntegerField(validators=[
        MinValueValidator(100, "La capacité doit être superieur de  0 kg")
    ])
    disponible=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)