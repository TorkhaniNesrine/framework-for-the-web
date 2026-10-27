from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from VehiculeApp.models import Vehicule
from .models import Entreprise, Utilisateur

# Register your models here.
class VehiculeInLine(admin.TabularInline) :
    model = Vehicule
    fields=("immatriculation","type_vehicule","capacite_kg","disponible")
    extra = 2
    show_change_link =  True

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    inlines=[VehiculeInLine]
    list_display = ('raison_social', 'matricule_fiscal', 'type_entreprise', 'gerant')
    list_filter = ('type_entreprise',)
    search_fields = ('raison_social', 'matricule_fiscal', 'gerant__username')
    list_editable = ('type_entreprise',)
    ordering = ('raison_social',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Informations de l'entreprise", {
            'fields': ('raison_social', 'matricule_fiscal', 'type_entreprise', 'adresse')
        }),
        ("Gérance", {
            'fields': ('gerant',)
        }),
        ("Dates & Historique", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
admin.site.site_header='TransConnect - Administration'
admin.site.site_title='TransConnect'
admin.site.index_title='Tableau de bord'

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('user_id', 'username', 'email', 'role', 'telephone', 'is_active','created_at')
    list_filter = ('role', 'is_active')
    search_fields = ('user_id', 'username', 'email', 'telephone')
    list_editable = ('role', 'telephone')
    ordering = ('user_id',)
    readonly_fields = ('user_id', 'date_joined', 'last_login', 'created_at', 'updated_at')

    fieldsets = (
        ("Informations personnelles & Compte", {
            'fields': ('user_id', 'username', 'email', 'role', 'telephone')
        }),
        ("Permissions & Statut", {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
            'classes': ('collapse',),
        }),
        ("Dates & Historique", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    add_fieldsets = (
        (
        None, {
                    'classes': ('wide',),
                    'fields': ('username', 'email', 'role', 'telephone', 'password1', 'password2','usable_password'),
                }),
                )

# admin.site.register(Entreprise, EntrepriseAdmin)
# admin.site.register(Utilisateur, UtilisateurAdmin)