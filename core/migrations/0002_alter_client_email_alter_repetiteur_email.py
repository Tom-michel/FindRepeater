# Generated by Django 4.0.1 on 2022-01-13 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='repetiteur',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
