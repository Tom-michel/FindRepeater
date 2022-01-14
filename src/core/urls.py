from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index'),
    path('inscriptionprof', views.inscriptionprof, name='inscriptionprof'),
    path('inscriptionClient', views.inscriptionClient, name='inscriptionClient'),
    path('connexionClient', views.connexionClient, name='connexionClient'),
    #path('connexionprof', views.connexionprof, name='connexionprof'),
    path('connexion', views.connexion, name='connexion'),
    path('recherche', views.recherche, name='recherche'),


]
