# Generated by Django 3.2 on 2023-05-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecotizacion',
            name='total_pagar',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
