# Generated by Django 3.2 on 2023-05-30 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20230529_1954'),
        ('materiales', '0001_initial'),
        ('cotizaciones', '0004_alter_detallecotizacion_total_pagar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='proyecto',
            field=models.OneToOneField(error_messages={'unique': 'Ya existe una cotización para este proyecto.'}, on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto'),
        ),
        migrations.AlterField(
            model_name='detallecotizacion',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detallecotizacion',
            name='materiales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.material'),
        ),
    ]
