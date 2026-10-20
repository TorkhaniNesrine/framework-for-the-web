from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin

from VehiculeApp.models import Vehicule
from .models import Utilisateur, Entreprise

admin.site.site_header = 'TransConnect - Administration'
admin.site.site_title = 'TransConnect'
admin.site.index_title = "Tableau de bord"

class VehiculeInline(admin.TabularInline):
    model = Vehicule
    fields = ('type_vehicule', 'capacite_kg', 'disponible')
    extra = 2
    show_change_link = True


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('user_id', 'username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('user_id', 'username', 'email')
    ordering = ('-date_joined',)
    readonly_fields = ('user_id',)

    fieldsets = UserAdmin.fieldsets + (
        ('Informations TransConnect', {
            'fields': ('user_id', 'telephone', 'role'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'telephone', 'role', 'password1', 'password2'),
        }),
    )


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    inlines = [VehiculeInline]
    list_display = ('raison_social', 'matricule_fiscal', 'type_entreprise', 'gerant', 'created_at')
    list_filter = ('type_entreprise',)
    search_fields = ('raison_social', 'matricule_fiscal')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informations générales', {
            'fields': ('raison_social', 'matricule_fiscal', 'type_entreprise')
        }),
        ('Contact et rattachement', {
            'fields': ('adresse', 'gerant')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
=======
from .models import Utilisateur, Entreprise

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'is_active', 'is_superuser', 'role')
    list_editable = ('username', 'is_active', 'is_superuser')
    search_fields = ('user_id', 'username', 'email')
    list_filter = ('is_active', 'is_superuser', 'role')
    list_per_page = 2

admin.site.register(Utilisateur, UserAdmin)
admin.site.register(Entreprise)
>>>>>>> 8dc741631e853031c30b08f9717f6a53c79944be
