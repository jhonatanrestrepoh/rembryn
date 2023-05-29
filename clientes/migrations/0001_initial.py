# Generated by Django 3.2 on 2023-05-29 15:21

import clientes.models
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
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(error_messages={'unique': 'Ya existe un usuario con esta cédula'}, max_length=10, unique=True, validators=[clientes.models.validate_cedula], verbose_name='Cédula')),
                ('primer_nombre', models.CharField(max_length=50, validators=[clientes.models.validate_not_contain_numbers])),
                ('segundo_nombre', models.CharField(blank=True, max_length=50, validators=[clientes.models.validate_not_contain_numbers])),
                ('primer_apellido', models.CharField(max_length=50, validators=[clientes.models.validate_not_contain_numbers])),
                ('segundo_apellido', models.CharField(blank=True, max_length=50, validators=[clientes.models.validate_not_contain_numbers])),
                ('celular', models.CharField(max_length=10, validators=[clientes.models.validate_celular])),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
