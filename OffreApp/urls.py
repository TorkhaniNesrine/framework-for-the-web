from django.urls import path
from . import views

app_name = 'offre'

urlpatterns = [
    path('classe/', views.Liste_offre.as_view(), name='liste_offre_classe'),
    path('classe/<int:pk>/', views.Detail_offre.as_view(), name='detail_offre'),
    path('supprimer/<int:pk>/', views.DeleteOffre.as_view(), name='supprimer_offre'),
    path('creer/', views.CreateOffre.as_view(), name='creer_offre'),
    path('modifier/<int:pk>/', views.UpdateOffre.as_view(), name='modifier_offre'),
]