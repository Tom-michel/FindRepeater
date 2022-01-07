from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.

class Classe(models.Model):
    niveau = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.niveau

class Matiere(models.Model):
    intitulé = models.CharField(max_length=200, null=True)

    #relation many-to-many avec Classe
    classeMat = models.ManyToManyField(Classe)

    def __str__(self):
        return self.intitulé

class Cours(models.Model):
    titre = models.CharField(max_length=200, null=True)

    #la clé de Matiere migre vers Cours
    matiere = models.ForeignKey(Matiere, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titre

class Enseignant(models.Model):
    CIVILITE = (('Mr','Mr'),
                ('Mme','Mme'),
                ('Mle','Mle'))
    dateNais = models.DateField(null=True)
    niveauEtude = models.CharField(max_length=200, null=True)
    photoProfil = models.ImageField
    ville = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True)
    civilité = models.CharField(max_length=200, null=True, choices=CIVILITE)
    prenom = models.CharField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    #relation many-to-many avec Classe
    classeEns = models.ManyToManyField(Classe)
    #relation many-to-many avec Matiere
    matiereEns = models.ManyToManyField(Matiere)

    def __str__(self):
        info = self.prenom+" "+self.nom
        return info

class Client(models.Model):
    CIVILITE = (('Mr','Mr'),
                ('Mme','Mme'),
                ('Mle','Mle'))
    civilité = models.CharField(max_length=200, null=True, choices=CIVILITE)
    prenom = models.CharField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    #relation many-to-many avec Cours
    coursCli = models.ManyToManyField(Cours)

    def __str__(self):
        info = self.prenom+" "+self.nom
        return info

