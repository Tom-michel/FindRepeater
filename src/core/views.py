from django.shortcuts import render
from .models import Client
from django.http import HttpResponse

def index(request):
    return render(request,'core/index.html')

def inscriptionprof(request):
    return render(request,'core/inscriptionprof.html')

# inscription du Client

def inscriptionClient(request):

    # enregistrement du client dans la BD
    if request.method == "POST":
        civilite = request.POST.get('civilite')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        client = Client()
    
    return render(request, 'core/inscriptionClient.html')

def connexionprof(request):
    return render(request, 'core/connexionprof.html')

def connexionClient(request):
    return render(request, 'core/connexionClient.html')

def recherche(request):
    return render(request, 'core/recherche.html')


