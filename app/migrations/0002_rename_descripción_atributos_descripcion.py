# Generated by Django 4.2 on 2023-04-09 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atributos',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
