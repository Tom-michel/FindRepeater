from django.db import models


# Creation de la table repetiteur

class Repetiteur(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    sexe = models.CharField(max_length=10)
    dateNais = models.DateField(verbose_name="date de naissance")
    telephone = models.IntegerField()
    ville = models.CharField(max_length=25)
    quartier = models.CharField(max_length=20)
    niveau_etude = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    photo = models.ImageField()

    class Meta:
        verbose_name = "Informations repetiteur"


# creation de la table jours qui vas contenir les jours de la semaine

class Jour(models.Model):
    nomJour = models.CharField(max_length=8)
