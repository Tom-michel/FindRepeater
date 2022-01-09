from django.db import models


# creation de la table abstract personne

class Person(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    class Meta:
        abstract = True


# creation de la classe Plateforme

class Plateforme(models.Model):

    class Meta:
        abstract = True
        verbose_name = "FindRepeater"


# Creation de la classe repetiteur qui est une personne

class Repetiteur(Person):
    sexe = models.CharField(max_length=10)
    dateNais = models.DateField(verbose_name="date de naissance")
    ville = models.CharField(max_length=25)
    quartier = models.CharField(max_length=20)
    niveau_etude = models.CharField(max_length=15)
    photo = models.ImageField()

    def modifierProfil(self):
        pass

    class Meta:
        verbose_name = "Informations repetiteur"


# creation de la classe client qui vas heriter des attribut de la classe personne

class Client(Person):

    class meta:
        verbose_name = "information client"


# creation de la classe matiere

class Matiere(models.Model):
    intitule = models.CharField(max_length=20, verbose_name="matiere")


# creation de la classe  Classe

class Classe(models.Model):
    niveau = models.CharField(max_length=15)


# creation de la classe Cours

class Cours(models.Model):
    idclasse = models.ForeignKey(Classe, null=False, on_delete=models.CASCADE)
    idmatiere = models.ForeignKey(Matiere, null=False, on_delete=models.CASCADE)
    repetiteur = models.ManyToManyField(Repetiteur)
    jour = models.CharField(max_length=8)
    heure = models.TimeField(verbose_name="horaire")