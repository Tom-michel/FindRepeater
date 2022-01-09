from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('connexion/inscription/', views.inscription, name='inscription'),
    path('parent/', views.parent, name='parent'),
    path('connexion/', views.connexio, name='connexio'),
]
