from django.contrib import admin
from .models import Expedition
class expeditionadmin(admin.ModelAdmin):
    
    list_display = ('reference', 'ville_depart', 'ville_arrive', 'poids_kg', 'statut', 'entreprise', 'date_souhaitee')
    list_editable = ('statut',)
    search_fields = ('reference', 'ville_depart', 'ville_arrive')
    list_filter = ('statut', 'ville_depart', 'ville_arrive')
    readonly_fields = ('reference', 'created_at', 'updated_at')
admin.site.register(Expedition, expeditionadmin)