from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'core/index.html')

def inscriptionprof(request):
    return render(request,'core/inscriptionprof.html')

def inscriptionClient(request):
    return render(request, 'core/inscriptionClient.html')

def connexionprof(request):
    return render(request, 'core/connexionprof.html')

def connexionClient(request):
    return render(request, 'core/connexionClient.html')

def recherche(request):
    return render(request, 'core/recherche.html')
def erreur404(request,exception):
    return render(request, 'core/erreur404.html')
def pageProfiles(request):
    return render(request, 'core/pageProfiles.html')
def profileRéglage(request):
    return render(request, 'core/profileRéglage.html')

