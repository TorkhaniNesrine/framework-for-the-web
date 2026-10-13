from django.contrib import admin
from .models import Utilisateur, Entreprise

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'is_active', 'is_superuser', 'role')
    list_editable = ('username', 'is_active', 'is_superuser')
    search_fields = ('user_id', 'username', 'email')
    list_filter = ('is_active', 'is_superuser', 'role')
    list_per_page = 2

admin.site.register(Utilisateur, UserAdmin)
admin.site.register(Entreprise)