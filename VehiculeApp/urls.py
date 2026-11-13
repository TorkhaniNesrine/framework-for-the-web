from django.urls import path
from . import views

app_name = 'vehicule'

urlpatterns = [
    path('classe/', views.Liste_vehicule.as_view(), name='liste_vehicule_classe'),
    path('classe/<int:pk>/', views.Detail_vehicule.as_view(), name='detail_vehicule'),
    path('supprimer/<int:pk>/', views.DeleteVehicule.as_view(), name='supprimer_vehicule'),
    path('creer/', views.CreateVehicule.as_view(), name='creer_vehicule'),
    path('modifier/<int:pk>/', views.UpdateVehicule.as_view(), name='modifier_vehicule'),
    path('modifier/<int:pk>/', views.UpdateVehicule.as_view(), name='modifier_vehicule'),
]