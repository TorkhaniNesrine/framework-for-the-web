from django.contrib import admin
from .models import Expedition
<<<<<<< HEAD
from django.utils import timezone
from EntrepriseApp.models import Entreprise
# Register your models here.
class EnRetardFilter(admin.SimpleListFilter):
    title = "en retard"
    parameter_name = "en_retard"

    def lookups(self, request, model_admin):
        return [("oui", "Oui"), ("non", "Non")]

    def queryset(self, request, queryset):
        aujourd_hui = timezone.now().date()
        if self.value() == "oui":
            return queryset.filter(statut="publiee", 
                                   date_souhaitee__lt=aujourd_hui)
        if self.value() == "non":
            return queryset.exclude(statut="publiee", 
                                    date_souhaitee__lt=aujourd_hui)
        return queryset
@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'entreprise', 'ville_depart', 'ville_arrivee', 'poids_kg', 'date_souhaitee', 'statut')
    list_filter = ('statut', 'date_souhaitee', 'entreprise',EnRetardFilter)
    search_fields = ('reference', 'ville_depart', 'ville_arrivee', 'entreprise__raison_social')
    list_editable = ('statut',)
    ordering = ('-created_at',)
    readonly_fields = ('reference', 'created_at', 'updated_at')

    fieldsets = (
        ("Informations générales", {
            'fields': ('reference', 'entreprise', 'statut')
        }),
        ("Détails logistiques", {
            'fields': ('ville_depart', 'ville_arrivee', 'poids_kg', 'date_souhaitee', 'description')
        }),
        ("Dates & Historique", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


=======
class expeditionadmin(admin.ModelAdmin):
    
    list_display = ('reference', 'ville_depart', 'ville_arrive', 'poids_kg', 'statut', 'entreprise', 'date_souhaitee')
    list_editable = ('statut',)
    search_fields = ('reference', 'ville_depart', 'ville_arrive')
    list_filter = ('statut', 'ville_depart', 'ville_arrive')
    readonly_fields = ('reference', 'created_at', 'updated_at')
admin.site.register(Expedition, expeditionadmin)
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
