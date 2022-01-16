from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('profil',views.profil,name='profil'),

    path('user/enseignant/register',views.inscriptionprof,name='inscriptionprof'),
    path('user/eleve_parent/register', views.inscriptionClient,name='inscriptionClient'),
    path('user/eleve_parent/login', views.connexionClient,name='connexionClient'),
    path('user/enseignant/login', views.connexionprof,name='connexionprof'),
    path('user/enseignant/list_repetiteur', views.list_rep, name='list_repetiteur'),
    path('user/enseignant/ajoutCours', views.ajoutCours, name='ajoutCours'),
    path('findrepeaper/recherche', views.recherche,name='recherche'),
    path('findrepeaper/recherche', views.redirect,name='redirect'),
    path('findrepeaper/resultatRecherche', views.resultatRecherche, name='resultatRecherche'),
    path('user_logout', views.user_logout,name='user_logout'),

]