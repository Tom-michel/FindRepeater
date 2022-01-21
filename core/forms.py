from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Client, Repetiteur, Cours

# formulaire pour l'iscrition du client en rassemblant de 2 formulaires :
        # User (fourni par django)
        # Client (notre classe créée dans models.py)

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
class RepetiteurForm(forms.ModelForm):
    class Meta():
        model = Repetiteur
        fields = [
            'type_user',
            'civilité',
            'age',
            'telephone',
            'photoProfil',
            'niveauEtude',
            'ville',
            'quartier',
            'langue'
        ]
class ClientForm(forms.ModelForm):
    class Meta():
        model = Client
        fields = [
            'type_user',
            'age',
            'civilité',
            'telephone',
            'photoProfil',
            'langue'
        ]
class CoursForm(forms.ModelForm):
    class Meta():
        model = Cours
        fields = [
            'jour',
            'heure_début',
            'duree',
            'matiere',
            'classe',
            'repetiteur'
        ]