# Generated by Django 4.0.1 on 2022-01-13 22:53

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repetiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilité', models.CharField(choices=[('Monsieur', 'Monsieur'), ('Mademoiselle', 'Mademoiselle'), ('Madame', 'Madame')], default='Monsieur', max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('photoProfil', models.ImageField(blank=True, upload_to=core.models.renommer_image)),
                ('type_user', models.CharField(choices=[('Élève', 'Élève'), ('Parent', 'Parent'), ('Enseignant', 'Enseignant')], default='Élève', max_length=200, null=True)),
                ('niveauEtude', models.CharField(max_length=200, null=True)),
                ('ville', models.CharField(max_length=200, null=True)),
                ('quartier', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(choices=[('lundi', 'lundi'), ('mardi', 'mardi'), ('mercredi', 'mercredi'), ('jeudi', 'jeudi'), ('vendredi', 'vendredi'), ('samedi', 'samedi'), ('dimanche', 'dimanche')], default='lundi', max_length=200, null=True)),
                ('heure_début', models.CharField(choices=[('7H', '7H'), ('8H', '8H'), ('9H', '9H'), ('10H', '10H'), ('11H', '11H'), ('12H', '12H'), ('13H', '13H'), ('14H', '14H'), ('15H', '15H'), ('16H', '16H'), ('17H', '17H'), ('18H', '18H')], default='7H', max_length=200, null=True)),
                ('duree', models.CharField(choices=[('1H', '1H'), ('1H30', '1H30'), ('2H', '2H'), ('2H30', '2H30'), ('3H', '3H')], default='2H', max_length=200, null=True)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.classe')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.matiere')),
                ('repetiteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.repetiteur')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilité', models.CharField(choices=[('Monsieur', 'Monsieur'), ('Mademoiselle', 'Mademoiselle'), ('Madame', 'Madame')], default='Monsieur', max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('photoProfil', models.ImageField(blank=True, upload_to=core.models.renommer_image)),
                ('type_user', models.CharField(choices=[('Élève', 'Élève'), ('Parent', 'Parent'), ('Enseignant', 'Enseignant')], default='Élève', max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
