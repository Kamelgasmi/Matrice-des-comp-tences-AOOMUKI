# Generated by Django 3.1.7 on 2021-03-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_matrice', '0005_auto_20210326_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborater',
            name='collaborater',
            field=models.BooleanField(default=True, verbose_name='Ajouter en tant que collaborateur ?'),
        ),
    ]