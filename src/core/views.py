from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, logout as django_logout, authenticate

from .models import Client
from .formulaire import Connexion


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

#def connexionprof(request):
    #return render(request, 'core/connexionprof.html')


def connexionClient(request):
    return render(request, 'core/connexionClient.html')

def recherche(request):
    return render(request, 'core/recherche.html')


def connexion(request):
    if request.method == 'POST':
        form = Connexion(data = request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                django_login(request,user)
                return redirect('rechercher') #user is redirected to dashboard
    else:
        form = Connexion()
        return render(request,'core/connexionprof.html',{'form':form,})

# fonction pou rechercher les enseignants
def recherche_repetiteur(request):
    
    recherche = render(request.Get.get('recherche'))
    print(recherche)
    return render(request, 'core/recerche.html',{'search':recherche})
