from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_email(value):
    if not value:
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def _generate_user_id(cls):
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

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()

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