# Generated by Django 3.2 on 2023-05-30 03:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0006_auto_20230529_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='descuento',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='detallecotizacion',
            name='cantidad',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]