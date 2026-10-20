from django.contrib import admin
from .models import Offre

# Register your models here.
class PrixFilter(admin.SimpleListFilter):
    title = "tranche de prix"
    parameter_name = "tranche_prix"

    def lookups(self, request, model_admin):
        return [
            ("bas", "Moins de 100 "),
            ("moyen", "Entre 100 € et 1000 "),
            ("eleve", "Plus de 1000 "),
        ]

    def queryset(self, request, queryset):
        if self.value() == "bas":
            return queryset.filter(prix__lt=100)
        if self.value() == "moyen":
            return queryset.filter(prix__gte=100, prix__lte=1000)
        if self.value() == "eleve":
            return queryset.filter(prix__gt=1000)
        return queryset
class OffreAdmin(admin.ModelAdmin):
    list_display = ('id', 'expedition', 'transporteur', 'vehicule', 'prix', 'delai_jours', 'statut')
    list_filter = ('statut', 'transporteur', 'date_proposition')
    search_fields = ('expedition__reference', 'transporteur__raison_social', 'vehicule__immatricule')
    list_editable = ('prix', 'delai_jours', 'statut')
    ordering = ('-date_proposition', '-created_at')
    readonly_fields = ('date_proposition', 'created_at', 'updated_at')

    fieldsets = (
        ("Parties prenantes", {
            'fields': ('expedition', 'transporteur', 'vehicule')
        }),
        ("Conditions de l'offre", {
            'fields': ('prix', 'delai_jours', 'statut')
        }),
        ("Dates & Historique", {
            'fields': ('date_proposition', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Offre, OffreAdmin)