# Generated by Django 3.2 on 2023-05-29 15:21

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direcciones', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('fecha_fin', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 5, 29))])),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('estados', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Validado', 'Validado'), ('Cotizado', 'Cotizado'), ('Cancelado', 'Cancelado'), ('Terminado', 'Terminado')], max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('direccion', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cliente', chained_model_field='cliente', on_delete=django.db.models.deletion.CASCADE, to='direcciones.direccion')),
            ],
        ),
    ]
