from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('inscriptionprof',views.inscriptionprof,name='inscriptionprof'),
    path('inscriptionClient', views.inscriptionClient,name='inscriptionClient'),
    path('connexionClient', views.connexionClient,name='connexionClient'),
    path('connexionprof', views.connexionprof,name='connexionprof'),
    path('user_logout', views.user_logout,name='user_logout'),
    path('recherche', views.recherche,name='recherche'),

]