# Generated by Django 4.0.1 on 2022-01-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_intitulé_matiere_intitule'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='heure',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='jour',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='repetiteur',
            name='photoProfil',
            field=models.ImageField(upload_to=''),
        ),
    ]
