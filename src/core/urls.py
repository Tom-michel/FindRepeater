from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('inscriptionprof',views.inscriptionprof,name='inscriptionprof'),
    path('inscriptionClient', views.inscriptionClient,name='inscriptionClient'),
    path('connexionClient', views.connexionClient,name='connexionClient'),
    path('connexionprof', views.connexionprof,name='connexionprof'),
    path('recherche', views.recherche,name='recherche'),
    path('pageProfiles', views.pageProfiles,name='pageProfiles'),
    path('profileRéglage', views.recherche,name='profileRéglage'),
    path('erreur404', views.erreur404,name='erreur404'),

]