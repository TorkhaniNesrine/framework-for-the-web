from django.db import models
<<<<<<< HEAD
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone


class Expedition(models.Model):
    reference = models.CharField(max_length=50, unique=True, editable=False)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_kg = models.PositiveIntegerField(
        validators=[MinValueValidator(1, "Ne pas accepter un poids nul.")]
    )
    date_souhaitee = models.DateField()
    description = models.TextField(blank=True, null=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('publiee', 'Publiée'),
            ('attribuee', 'Attribuée'),
            ('en_cours', 'En cours'),
            ('livree', 'Livrée'),
            ('annulee', 'Annulée'),
        ],
        default='publiee',
    )
    entreprise = models.ForeignKey(
        'EntrepriseApp.Entreprise',
        on_delete=models.CASCADE,
        related_name='expeditions'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'chargeur':
            raise ValidationError({'entreprise': "Une expédition ne peut être créée que par une entreprise de type chargeur."})

    @classmethod
    def _generate_ref(cls):
        annee = timezone.now().strftime('%y')
        prefixe = f"EXP-{annee}-"
        dernier = cls.objects.filter(reference__startswith=prefixe).order_by('reference').last()
        compteur = (int(dernier.reference.split('-')[-1]) + 1) if dernier else 1
        if compteur > 99999:
            raise ValidationError("Limite de 99999 expéditions atteinte pour cette année.")
        return f"{prefixe}{compteur:05d}"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_ref()
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} ({self.statut})"

        
        
   
=======
from EntrepriseApp.models import Entreprise
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
class Expedition(models.Model):
    reference = models.CharField(max_length=50, unique=True)
    ville_depart = models.CharField(max_length=80)
    ville_arrive = models.CharField(max_length=80)

    poids_kg = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        validators=[
            MinValueValidator(0.001, "Le poids doit être supérieur à 0 kg"),
        ]
    )

    date_souhaitee = models.DateTimeField()
    description = models.TextField()

    statut = models.CharField(
        max_length=100,
        choices=[
            ('en_attente', 'en_attente'),
            ('t', 'terminee'),
            ('a', 'annulee')
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='entreprise'
    )
    def clean(self):
         super().clean()
         if self.entreprise_id and self.entreprise.type_entreprise !='chargeur' :
             raise ValidationError("l'entreprise : une expedition ne peut crée que paar un chargeur ")
    
    @classmethod
    def _generate_reference(cls):
        annee = timezone.now().strftime('%Y')
        prefix = f"EXP-{annee}-"

        dernier = (
            cls.objects
            .filter(reference__startswith=prefix)
            .order_by('reference')
            .last()
        )

        compteur = (
            int(dernier.reference[-5:]) + 1
            if dernier
            else 1
        )

        if compteur > 99999:
            raise ValueError("Limite dépassée")

        return f"{prefix}{compteur:05d}"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()

        self.full_clean()

        super().save(*args, **kwargs)
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
