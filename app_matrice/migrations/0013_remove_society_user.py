# Generated by Django 3.1.7 on 2021-04-08 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_matrice', '0012_society_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='society',
            name='user',
        ),
    ]
