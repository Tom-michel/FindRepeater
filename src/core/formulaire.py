from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.db.models.base import Model
from .models import Client
         



class Connexion(forms.Form):
    #email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
    #'type':'text','name': 'email','placeholder':'email'}), label='Email')
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
    #'type':'password', 'name':'password','placeholder':'Password'}),label='Mot de passe')
    class Meta:
        
        Model = Client
        fields = ['email', 'password']

    #def __init__(self, *args, **kwargs):
        #admin_check = kwargs.pop('admin_check', False)
        #super(Connexion, self).__init__(*args, **kwargs)
        #if not admin_check:
            #del self.fields['admin']    
    