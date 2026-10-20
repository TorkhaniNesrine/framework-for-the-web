from django.contrib import admin
from .models import Vehicule

# Register your models here.

<<<<<<< HEAD
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatricule', 'type_vehicule', 'disponible', 'capacite_kg', 'entreprise')
    list_filter = ('disponible', 'type_vehicule', 'entreprise')
    search_fields = ('immatricule', 'type_vehicule', 'entreprise__raison_social')
    list_editable = ('type_vehicule', 'disponible', 'capacite_kg')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Informations générales", {
            'fields': ('immatricule', 'type_vehicule', 'capacite_kg', 'disponible')
        }),
        ("Entreprise associée", {
            'fields': ('entreprise',)
        }),
        ("Dates & Historique", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Vehicule, VehiculeAdmin)
=======
@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'type_vehicule', 'disponible')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identification', {
            'fields': ('immatriculation', 'type_vehicule', 'capacite_kg')
        }),
        ('Statut', {
            'fields': ('disponible',)
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
