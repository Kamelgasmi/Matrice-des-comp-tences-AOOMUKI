# Generated by Django 3.1.7 on 2021-04-08 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_matrice', '0009_auto_20210402_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur '),
        ),
    ]
