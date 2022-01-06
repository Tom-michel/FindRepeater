from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomeView(View):
   template_name = "core/index.html"

class ConnexionView(View):
   template_name = "core/connexion.html"
      
class InscriptionensView(View):
   template_name = "core/inscriptionEns.html"
         
class InscriptionView(View):
   template_name = "core/inscription.html"

