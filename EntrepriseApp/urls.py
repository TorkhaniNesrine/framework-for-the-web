from django.urls import path
from . import views

app_name = 'entreprise'

urlpatterns = [
    path('classe/', views.Liste_entreprise.as_view(), name='liste_entreprise_classe'),
    path('classe/<int:pk>/', views.Detail_entreprise.as_view(), name='detail_entreprise'),
    path('supprimer/<int:pk>/', views.DeleteEntreprise.as_view(), name='supprimer_entreprise'),
    path('creer/', views.CreateEntreprise.as_view(), name='creer_entreprise'),
    path('modifier/<int:pk>/', views.UpdateEntreprise.as_view(), name='modifier_entreprise'),
]