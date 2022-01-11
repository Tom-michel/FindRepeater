from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
import os

# Create your models here.

# creation de la classe Classe

class Classe(models.Model):
    niveau = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.niveau

# creation de la classe Matiere

class Matiere(models.Model):
    intitule = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.intitule

# creation de la classe cours

class Cours(models.Model):
    jour = models.CharField(max_length=200, null=True)
    heure = models.TimeField(null=True)

    # un Cours a une seulle Matiere
    matiere = models.ForeignKey(Matiere, null=True, on_delete=models.CASCADE)

    # un Cours concerne une seule Classe
    classe = models.ForeignKey(Classe, null=True, on_delete=CASCADE)

    def __str__(self):
        info = self.matiere.intitule+" "+self.classe.niveau
        return info


# creation la classe Utilisateur

def renommer_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "photo_profile/{}.{}".format(instance.user.username, ext)
        return os.path.join(upload_to, filename)


class Utilisateur(models.Model):
    Monsieur = 'Monsieur'
    Mademoiselle = 'Mademoiselle'
    Madame = 'Madame'
    CIVILITE = [
        (Monsieur,'Monsieur'),(Mademoiselle,'Mademoiselle'),(Madame,'Madame')
    ]
    civilité = models.CharField(max_length=200, null=True, choices=CIVILITE, default=Monsieur)
    
    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=CASCADE)
    
    telephone = models.CharField(max_length=200, null=True)
    photoProfil = models.ImageField(upload_to=renommer_image) 

    # s'inscrire sur la platefoerme
    def inscrire():
        pass
    
    # se connecter à son compte
    def connecter():
        pass

    class Meta:
        abstract = True

# creation de la classe Client(élève/parent d'élève) qui est un Utilisateur

class Client(Utilisateur):
    TYPE_USER = [
        ('Élève','Élève'),('Parent','Parent')
    ]
    type_user = models.CharField(max_length=200, null=True, choices=TYPE_USER, default='Élève')
    def __str__(self):
        info = self.civilité+" "+self.user.username
        return info
    
    # rechercher un Repetiteur
    def rechercher(self, matiere, classe, ville, quartier):
        pass

    # consulter le profil d'un Repetiteur
    def consulterProfil(sel, repetiteur):
        pass


# creation de la classe Repetiteur qui est un Utilisateur

class Repetiteur(Utilisateur):
    TYPE_USER = [('Enseignant','Enseignant')]
    type_user = models.CharField(max_length=200, null=True, choices=TYPE_USER, default='Enseignant')
    dateNais = models.DateField(null=True)
    niveauEtude = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True) 

    # un Reptiteur donne plusieurs Cours
    listCours = models.ManyToManyField(Cours)

    def __str__(self):
        info = self.civilité+" "+self.prenom+" "+self.nom
        return info
   
    # s'inscrire : redefinir la methdode inscrire() de Utilisateur
    def inscrire():
        pass

    # modifier son profil (deja inscrit)
    def modifierProfil(self):
        pass
