from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
from django.core.validators import MinLengthValidator, RegexValidator
=======
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_email(value):
    if not value:
<<<<<<< HEAD
        raise ValidationError("L'adresse e-mail est obligatoire.")
    if not value.lower().endswith('@gmail.com'):
        raise ValidationError("Seuls les emails appartenant au domaine gmail.com sont acceptés.")


class Utilisateur(AbstractUser):
    user_id = models.CharField(max_length=8, primary_key=True, editable=False)
    email = models.EmailField(unique=True, validators=[validate_email])
    role = models.CharField(
        max_length=20,
        choices=[
            ('chargeur', 'Chargeur'),
            ('transporteur', 'Transporteur'),
            ('admin', 'Admin')
        ],
        default='chargeur'
    )
    telephone = models.CharField(max_length=20, blank=True, null=True)
=======
        raise ValidationError("L'adresse email est obligatoire")
    if not value.endswith('@gmail.com'):
        raise ValidationError("Le domaine accepté est gmail")


matricule_fiscale_validator = RegexValidator(
    regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
    message="Format erroné"
)


class Utilisateur(AbstractUser):
    user_id = models.CharField(
        primary_key=True,
        max_length=8
    )

    email = models.EmailField(
        unique=True,
        validators=[validate_email]
    )

    telephone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Admin'),
            ('c', 'Chargeur'),
            ('t', 'Transporteur'),
        ],
        default='c'
    )

>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def _generate_user_id(cls):
<<<<<<< HEAD
        annee = timezone.now().strftime('%y')
        prefixe = f"{annee}user"
        dernier = cls.objects.filter(user_id__startswith=prefixe).order_by('user_id').last()
        compteur = (int(dernier.user_id[-2:]) + 1) if dernier else 0
        if compteur > 99:
            raise ValidationError("Limite de 99 utilisateurs atteinte pour cette année (00-99).")
        return f"{prefixe}{compteur:02d}"
=======
        year = timezone.now().year
        prefix = f"{year % 100:02d}user"

        last = (
            cls.objects
            .filter(user_id__startswith=prefix)
            .order_by('-user_id')
            .first()
        )

        n = int(last.user_id[-2:]) + 1 if last else 0

        if n > 99:
            raise ValidationError(
                f"Limite de 100 utilisateurs atteinte pour l'année {year}."
            )

        return f"{prefix}{n:02d}"
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()
<<<<<<< HEAD
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.user_id})"


matricule_fiscal_validator = RegexValidator(
    regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
    message="Format du Matricule Fiscal invalide (exemple: 1234567AAM000 ou 1234567/A/A/M/000)"
)


class Entreprise(models.Model):
    raison_social = models.CharField(max_length=200)
    matricule_fiscal = models.CharField(
        max_length=20,
        unique=True,
        validators=[matricule_fiscal_validator]
    )
    type_entreprise = models.CharField(
        max_length=20,
        choices=[
            ('chargeur', 'Chargeur'),
            ('transporteur', 'Transporteur'),
        ],
        default='chargeur'
    )
    adresse = models.TextField(
        validators=[MinLengthValidator(20, "L'adresse doit comporter au minimum 20 caractères.")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gerant = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entreprise')

    def __str__(self):
        return self.raison_social



=======

        self.full_clean()
        super().save(*args, **kwargs)


class Entreprise(models.Model):
    raison_social = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )

    matricule_fiscale = models.CharField(
        max_length=17,
        unique=True,
        validators=[matricule_fiscale_validator]
    )

    adresse = models.TextField(
        validators=[
            MinLengthValidator(
                20,
                "L'adresse ne peut pas avoir moins de 20 caractères."
            ),
            MaxLengthValidator(
                400,
                "L'adresse ne peut pas dépasser 400 caractères."
            )
        ]
    )

    type_entreprise = models.CharField(
        max_length=100,
        choices=[
            ('c', 'Chargeur'),
            ('t', 'Transporteur'),
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    gerant = models.OneToOneField(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='entreprise'
    )
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
