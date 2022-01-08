from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,
name='index'),
    path('inscription',views.inscription,
name='inscription'),
    path('parent', views.parent,
name='parent'),
    path('connexio', views.connexio,
name='connexio'),
]