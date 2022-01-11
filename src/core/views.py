from django.shortcuts import render
from .forms import UserForm, ClientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'core/index.html')

def inscriptionprof(request):
    return render(request,'core/inscriptionprof.html')

# fonction permettant l'inscription du Client avec enregistrement dans la BD

def inscriptionClient(request):
    registered = False
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
            print(user_form.errors, client_form.errors)

    else:
        user_form = UserForm()
        client_form = ClientForm()

    content = {
        'registered':registered,
        'form1':user_form,
        'form2':client_form,
    }
    return render(request, 'core/inscriptionClient.html', content)

# fonction permettant la connection du Client à son compte

def connexionClient(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("L'utilisateur est désactivé")
        else:
            return HttpResponse("Votre nom d'utilisateur ou votre mot de passe est incorrect")
    else:
        return render(request, 'core/connexionClient.html')


# fonction permettant de se déconnecter

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def connexionprof(request):
    return render(request, 'core/connexionprof.html')

def recherche(request):
    return render(request, 'core/recherche.html')


