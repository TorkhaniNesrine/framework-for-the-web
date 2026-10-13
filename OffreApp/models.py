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

    def clean(self):
        super().clean()

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