# Generated by Django 3.1.7 on 2021-04-08 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_matrice', '0010_society_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='society',
            name='user',
        ),
    ]
