# Generated by Django 3.2 on 2023-05-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas_tecnicas', '0002_alter_visitatecnica_fecha_visita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitatecnica',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
