
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from ExpeditionApp.views import register

urlpatterns = [
    path('admin/', admin.site.urls),

    # Applications
    path('expedition/', include('ExpeditionApp.urls')),
    path('entreprises/', include('EntrepriseApp.urls')),
    path('offres/', include('OffreApp.urls')),
    path('vehicules/', include('VehiculeApp.urls')),

    # Connexion
    path('login/', LoginView.as_view(
        template_name='expedition/login.html'
    ), name='login'),

    # Déconnexion
    path('logout/', LogoutView.as_view(), name='logout'),

    # Inscription
    path('register/', register, name='register'),
]
