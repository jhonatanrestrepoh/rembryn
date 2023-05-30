# Generated by Django 3.2 on 2023-05-29 23:18

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tecnicos', '0001_initial'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 29), message='La fecha debe ser igual o posterior a 29-05-2023.')]),
        ),
        migrations.CreateModel(
            name='DetallesProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_visita', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 29))])),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('descripcion', models.TextField(max_length=500)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto')),
                ('tecnicos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecnicos.tecnico')),
            ],
        ),
    ]