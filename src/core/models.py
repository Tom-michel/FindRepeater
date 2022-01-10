from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
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

class Utilisateur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

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

    def __str__(self):
        info = self.prenom+" "+self.nom
        return info
    
    # rechercher un Repetiteur
    def rechercher(self, matiere, classe, ville, quartier):
        pass

    # consulter le profil d'un Repetiteur
    def consulterProfil(sel, repetiteur):
        pass


# creation de la classe Repetiteur qui est un Utilisateur

class Repetiteur(Utilisateur):
    CIVILITE = (('Mr','Mr'),
                ('Mme','Mme'))
    civilité = models.CharField(max_length=200, null=True, choices=CIVILITE)
    dateNais = models.DateField(null=True)
    niveauEtude = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True)
    photoProfil = models.ImageField()  

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
