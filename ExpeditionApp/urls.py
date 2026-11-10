from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=False)),
    path('home/', views.home, name="home"),
    path('w/<str:name>', views.welcome, name="welcomeFunction"),
    path('list/', views.listExpeditions, name="list"),
    path('details/<int:id>/', views.detailsExpedition, name='detail'),
    path('Liste_expedition/', views.Liste_expedition.as_view(), name='liste_classe'),
    path('detail_expedition/<int:id>/', views.Detail_expedition.as_view(), name='detail_classe'),
    path('delete_expedition/<int:pk>/', views.DeleteExpedition.as_view(), name='delete'),
    path('createclass/', views.CreateExpedition.as_view(), name='create_expedition'),
    path('update_expedition/<int:pk>/', views.UpdateExpedition.as_view(), name='update_expedition'),
]