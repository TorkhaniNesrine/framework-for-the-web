from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('w/<str:name>', views.welcome, name="welcomeFunction"),
    path('list/', views.listExpeditions, name="list"),
    
    # Attention ici : c'est detailsExpedition (avec un s)
    path('details/<int:id>/', views.detailsExpedition, name='detail'),
]