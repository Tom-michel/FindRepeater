from typing import OrderedDict
from django.shortcuts import render
from .forms import UserForm, ClientForm, RepetiteurForm, CoursForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Classe, Matiere, Repetiteur, Client, Cours
from django.contrib.auth.models import User

def index(request):
    listR = Repetiteur.objects.all()
    listCours = Cours.objects.all()
    listRep = []
    for rep in listR:
        listRep.append(rep.user.username)
    content = {'listRep':listRep,'listCours':listCours}
    return render(request,'core/index.html', content)

def devProf(request):
    return render(request, 'core/inscriptionprof01.html')

def profilDave(request):
    return render(request, 'core/profil(dave).html')


def profilReg(request, pk, pu):

    err = ''
    err2 = ''
    coursList = Cours.objects.all()
    repList = Repetiteur.objects.all()
    repetiteur = Repetiteur.objects.get(id=pk)
    for u in User.objects.all():
        if u.id == repetiteur.user.id:
            user = User.objects.get(id=pu)
    
    rep_form = RepetiteurForm(instance=repetiteur)
    user_form = UserForm(instance=user)
    if request.method == "POST":
        rep_form = RepetiteurForm(data=request.POST, instance=repetiteur)
        user_form = UserForm(data=request.POST, instance=user)
        
        if rep_form.is_valid() and user_form.is_valid:
            rep = rep_form.save()
            rep.save()

            use = user_form.save()
            use.save()
            repetit = rep_form.save(commit=False)
            repetit.user = use
            repetit.save()
            return HttpResponseRedirect('../../monProfil')
        else:
            err = rep_form.errors
            err2 = user_form.errors
    content = {
        'err':err,
        'err2':err2,
        'rep_form':rep_form,
        'user_form':user_form,
        'coursList':coursList,
        'repList':repList,
    }
    return render(request,'core/profileReglage.html', content)

    # coursList = Cours.objects.all()
    # repList = Repetiteur.objects.all()

    # content = {'coursList':coursList, 'repList':repList}
    # return render(request,'core/profileReglage.html', content)


def rech(request):
    return render(request,'core/recherche2.html')


# afficher la liste des utilisateurs

@login_required(login_url='connexionClient')
def list_rep(request):
    rep = Repetiteur.objects.all()
    client_temp = Client.objects.all()
    clients = []
    for cli in client_temp:
        if cli.type_user == "??l??ve":
            clients.append(cli)

    content = {'rep':rep, 'clients':clients}
    return render(request, 'core/list_repetiteur.html', content)

# recherche de r??p??titeurs

@login_required(login_url='connexionClient')
def recherche(request):
    #recuperer les donn??es du formulaire
    if request.method == 'POST':
        matiere = request.POST.get('matiere')
        classe = request.POST.get('classe')
        ville = request.POST.get('ville')
        listCours = []
        listCoursEnseigne = []
        listCoursTemp = Cours.objects.all()
        for cours in listCoursTemp:
            if cours.matiere.intitule==matiere and cours.classe.niveau==classe and cours.repetiteur.ville==ville:
                listCours.append(cours)
                for c in Cours.objects.all():
                    if cours.repetiteur.user.username == c.repetiteur.user.username:
                        listCoursEnseigne.append(c.matiere.intitule)
        
        # retirer les doublons
        listC = []
        for cour in listCoursEnseigne:
            if cour not in listC:
                listC.append(cour)
        listC.sort()
        
        content = {'listCours':listCours, 'listC':listC}
        # return HttpResponseRedirect('../../findrepeaper/resultatRecherche')
        return render(request, 'core/pageProfiles.html', content)
    else:
        matiereList = Matiere.objects.all()
        classeList = Classe.objects.all()
        coursList = Cours.objects.all()
        villeList = []
        # liste des villes ?? proposer lors de la recherche
        for cours in coursList:
            if cours.repetiteur.ville not in villeList:
                villeList.append(cours.repetiteur.ville)
        villeList.sort()
        
        content = {
            'matiereList':matiereList,
            'classeList':classeList,
            'villeList':villeList
        }
        
        return render(request, 'core/recherche.html', content)

# les enseignant correspondant aux crit??res de recherche

def pageProfiles(request):

    return render(request,'core/pageProfiles.html')


# afficher les r??p??titeurs apr??s la recherche

def resultatRecherche(request):
    return render(request, 'core/resultatRecherche.html')


# consulter le profil d'un enseignant apr??s la recherche

def consulterProfil(request, pk):
    cours = Cours.objects.get(id=pk)
    coursList = Cours.objects.all()
    content = {'cours':cours, 'coursList':coursList}
    return render(request,'core/profilEns.html', content)


# la page o?? un enseignat peut visualiser/mofier son profil

@login_required(login_url='connexionprof')
def monProfil(request):
    coursList = Cours.objects.all()
    coursTemp = Cours.objects.all()
    cours = []
    for c in coursTemp:
        cours.append(c.repetiteur.user.id)

    repList = Repetiteur.objects.all()

    content = {'coursList':coursList, 'cours':cours,'repList':repList}
    return render(request, 'core/monProfil.html', content)



# incription
#def inscription(request, formUser, formUtil, path_fichier):
    registered = False
    err1 = " "
    err2 = " "
    if request.method == "POST":
        user_form = formUser(data=request.POST)
        client_form = formUtil(data=request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            registered = True
            return HttpResponseRedirect('login')
        else:
            err1 = user_form.errors
            err2 = client_form.errors
            print(user_form.errors, client_form.errors)

    else:
        user_form = UserForm()
        client_form = ClientForm()

    content = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':client_form,
    }
    return render(request, path_fichier, content)


# fonction permettant l'inscription du Client avec enregistrement dans la BD

def inscriptionClient(request):
    registered = False
    err1 = " "
    err2 = " "
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            registered = True
            return HttpResponseRedirect('login')
        else:
            err1 = user_form.errors
            err2 = client_form.errors
            # print(user_form.errors, client_form.errors)

    else:
        user_form = UserForm()
        client_form = ClientForm()

    content = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':client_form,
    }
    return render(request, 'core/inscriptionClient.html', content)

# fonction permettant la connection du Client ?? son compte

def connexionClient(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            lisUSer = []
            if user.is_active:
                clients = Client.objects.all()
                userAct = username
                for cli in clients:
                    lisUSer.append(cli.user.username)
                
                if userAct in lisUSer:
                    login(request, user)
                    return HttpResponseRedirect('../../findrepeaper/recherche')
                else:
                    msg1 = messages.info(request, "cet utilisateur ne correspond pas ?? un compte Parent ou ??l??ve !")
                content1 = {
                    'msg1':msg1
                }
                return render(request, 'core/connexionClient.html', content1)
            else:
                return HttpResponse("L'utilisateur est d??sactiv??")
        else:
            msg = messages.info(request, "votre Nom d'utilisateur ou votre Mot de passe est incorrect, veuillez r??essayer SVP !")
            content = {
                'msg':msg
            }
            return render(request, 'core/connexionClient.html', content)
    else:
        return render(request, 'core/connexionClient.html')


# fonction permettant l'inscription du Repetiteur avec enregistrement dans la BD

def inscriptionprof(request):
    registered = False
    err1 = " "
    err2 = " "
    if request.method == "POST":
        repetiteur_form = RepetiteurForm(data=request.POST)
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() and repetiteur_form.is_valid():
            user = user_form.save()
            user.save()
            repetiteur = repetiteur_form.save(commit=False)
            repetiteur.user = user
            repetiteur.save()
            registered = True
            #return HttpResponseRedirect('ajoutCours')
            return HttpResponseRedirect('login')
        else:
            err1 = user_form.errors
            err2 = repetiteur_form.errors
            #print(user_form.errors, repetiteur_form.errors)
    else:
        user_form = UserForm()
        repetiteur_form = RepetiteurForm()
    content = {
        'registered':registered,
        'err1':err1,
        'err2':err2,
        'form1':user_form,
        'form2':repetiteur_form,
    }
    return render(request,'core/inscriptionprof.html', content)


# fonction permettant la connection du Client ?? son compte

def connexionprof(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            lisUSer = []
            if user.is_active:
                repetiteurs = Repetiteur.objects.all()
                userAct = username
                for rep in repetiteurs:
                    lisUSer.append(rep.user.username)
                
                if userAct in lisUSer:
                    login(request, user)
                    return HttpResponseRedirect('monProfil')
                    # return HttpResponseRedirect('ajoutCours')
                else:
                    msg1 = messages.info(request, "cet utilisateur ne correspond pas ?? un compte Enseignant !")
                content1 = {
                    'msg1':msg1
                }
                return render(request, 'core/connexionprof.html', content1)
            else:
                return HttpResponse("L'utilisateur est d??sactiv??")
        else:
            msg = messages.info(request, "votre Nom d'utilisateur ou votre Mot de passe est incorrect, veuillez r??essayer SVP !")
            content = {
                'msg':msg
            }
            return render(request, 'core/connexionprof.html', content)
    else:
        return render(request, 'core/connexionprof.html')


#redirection la page recherche d'un enseignant lorsqu'un client est d??ja connect??

def redirect(request):
    matiereList = Matiere.objects.all()
    classeList = Classe.objects.all()
    coursList = Cours.objects.all()
    villeList = []
    for cours in coursList:
        if cours.repetiteur.ville not in villeList:
            villeList.append(cours.repetiteur.ville)
    villeList.sort()

    content = {
        'matiereList':matiereList,
        'classeList':classeList,
        'villeList':villeList
    }
    return render(request,'core/recherche.html',content)


# ajout d'un cours par l'enseignant

@login_required(login_url='inscriptionprof')
def ajoutCours(request):
    err = ''
    coursList = Cours.objects.all()
    if request.method == "POST":
        cours_form = CoursForm(data=request.POST)
        if cours_form.is_valid():
            cours = cours_form.save()
            cours.save()

            coursList = Cours.objects.all()
            return HttpResponseRedirect('monProfil')
        else:
            err = cours_form.errors
    else:
        cours_form = CoursForm()
    content = {
        'err':err,
        'cours_form':cours_form,
        'coursList':coursList,
    }
    return render(request,'core/ajoutCours.html', content)


# suppression d'un cours par l'enseignant

@login_required(login_url='inscriptionprof')
def supprimer(request, pk):
    cours = Cours.objects.get(id=pk)
    if request.method == 'POST':
        cours.delete()
        return HttpResponseRedirect('../monProfil')
    content = {'cours':cours}
    return render(request, 'supprimer.html', content)


# modification d'un cours par l'enseignant

@login_required(login_url='inscriptionprof')
def modifCours(request, pk):
    err = ''
    coursList = Cours.objects.all()
    coursM = Cours.objects.get(id=pk)
    cours_form = CoursForm(instance=coursM)

    if request.method == "POST":
        cours_form = CoursForm(data=request.POST, instance=coursM)
        if cours_form.is_valid():
            cours = cours_form.save()
            cours.save()

            coursList = Cours.objects.all()
            return HttpResponseRedirect('../monProfil')
        else:
            err = cours_form.errors
    content = {
        'err':err,
        'cours_form':cours_form,
        'coursList':coursList,
    }
    return render(request,'core/ajoutCours.html', content)



# fonction permettant de se d??connecter

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
