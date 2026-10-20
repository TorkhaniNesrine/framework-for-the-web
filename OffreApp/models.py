<<<<<<< HEAD
from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Offre(models.Model):
    STATUT_CHOICES = [
        ('proposee', 'Proposée'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
    ]

    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'), "Le prix doit être strictement supérieur à 0.")]
    )
    delai_jours = models.PositiveIntegerField(
        validators=[MinValueValidator(1, "Le délai doit être supérieur ou égal à 1 jour.")]
    )
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='proposee',
    )
    date_proposition = models.DateField(auto_now_add=True)

    expedition = models.ForeignKey(
        'ExpeditionApp.Expedition',
        on_delete=models.CASCADE,
        related_name='offres',
    )

    transporteur = models.ForeignKey(
        'EntrepriseApp.Entreprise',
        on_delete=models.CASCADE,
        related_name='offres_proposees',
    )

    vehicule = models.ForeignKey(
        'VehiculeApp.Vehicule',
        on_delete=models.CASCADE,
        related_name='offres',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
from django.db import models
from EntrepriseApp.models import Entreprise
from VehiculeApp.models import Vehicule
from ExpeditionApp.models import Expedition
from django.core.exceptions import ValidationError


# Create your models here.
class offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    delai_jours = models.PositiveIntegerField()
    statut = models.CharField(max_length=100, choices=[
        ('p', 'proposee'),
        ('a', 'acceptee'),
        ('r', 'refusee'),
        ('re', 'retiree')
    ], default='p')
    date_proposition = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='offres')
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE, related_name='offres')
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='offres')
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be

    def clean(self):
        super().clean()

<<<<<<< HEAD
        # R1 
        if self.transporteur_id and self.transporteur.type_entreprise != 'transporteur':
            raise ValidationError({
                'transporteur': "Une offre ne peut être créée que par une entreprise dont type_entreprise = transporteur."
            })

        # R2 
        if self.vehicule_id and self.transporteur_id and self.vehicule.entreprise_id != self.transporteur_id:
            raise ValidationError({
                'vehicule': "Le véhicule associé à une offre doit appartenir à la même entreprise que le transporteur de l'offre."
            })

        # R3 
        if not self.pk and self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError({
                'expedition': "Une expédition ne peut recevoir de nouvelles offres que si son statut est 'publiee'."
            })

        # R4 
        if self.statut == 'proposee' and self.transporteur_id and self.expedition_id:
            doublon = Offre.objects.filter(
                expedition_id=self.expedition_id,
                transporteur_id=self.transporteur_id,
                statut='proposee'
            )
            if self.pk:
                doublon = doublon.exclude(pk=self.pk)
            if doublon.exists():
                raise ValidationError(
                    "Une entreprise ne peut pas avoir deux offres au statut 'proposée' actives simultanément sur la même expédition."
                )

        # R6
        if not self.pk and self.vehicule_id and not self.vehicule.disponible:
            raise ValidationError({
                'vehicule': "Un véhicule dont disponible = False ne peut pas être proposé sur une nouvelle offre."
            })

        # R7 
        if self.vehicule_id and self.expedition_id:
            CAPACITE_MAX = {
                'camionnette':    1_500,   
                'fourgon':        3_500,   
                'camion_porteur': 19_000,  
                'semi_remorque':  26_000,  
            }
            capacite = CAPACITE_MAX.get(self.vehicule.type_vehicule)
            if capacite is not None and self.expedition.poids_kg > capacite:
                raise ValidationError({
                    'vehicule': (
                        f"Le véhicule de type '{self.vehicule.type_vehicule}' "
                        f"ne peut pas transporter {self.expedition.poids_kg} kg "
                        f"(capacité maximale : {capacite} kg)."
                    )
                })

    def save(self, *args, **kwargs):
        # ? (R5)
        statut_precedent = None
        if self.pk:
            try:
                statut_precedent = Offre.objects.get(pk=self.pk).statut
            except Offre.DoesNotExist:
                pass

        self.full_clean()
        super().save(*args, **kwargs)

        # R5 
        if self.statut == 'acceptee' and statut_precedent != 'acceptee':
            expedition = self.expedition
            expedition.statut = 'attribuee'
            expedition.save()

            Offre.objects.filter(
                expedition_id=self.expedition_id,
                statut='proposee'
            ).exclude(pk=self.pk).update(statut='refusee')

    def __str__(self):
        return f"Offre {self.id} ({self.prix} DT) - {self.statut}"

=======
        if self.entreprise_id and self.entreprise.type_entreprise != 't':
            raise ValidationError("Une offre ne peut pas être faite que par un transporteur.")

        if self.vehicule_id and self.vehicule.entreprise_id != self.entreprise_id:
            raise ValidationError("Le véhicule associé à l'offre doit appartenir à la même entreprise que l'offre.")

        if self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError("L'expédition associée à l'offre doit être publiée pour pouvoir recevoir des offres.")

        if offre.objects.filter(entreprise_id=self.entreprise_id, expedition_id=self.expedition_id, statut='p').exclude(pk=self.pk).exists():
            raise ValidationError("Cette entreprise a déjà une offre proposée pour cette expédition.")

        if self.vehicule_id and not self.vehicule.disponible:
            raise ValidationError("Ce véhicule n'est pas disponible pour une nouvelle offre.")

        if self.vehicule_id and self.expedition_id:
            capacite_max = self.CAPACITES_INDICATIVES.get(self.vehicule.type_vehicule, 0)
            if self.expedition.poids_kg > capacite_max:
                raise ValidationError("Le poids de l'expédition dépasse la capacité du véhicule.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.statut == 'acceptee' and self.expedition_id:
            self.expedition.statut = 'attribuee'
            self.expedition.save()

            offre.objects.filter(expedition_id=self.expedition_id, statut='p').exclude(pk=self.pk).update(statut='r')
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
