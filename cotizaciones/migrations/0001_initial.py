# Generated by Django 3.2 on 2023-05-30 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materiales', '0001_initial'),
        ('proyectos', '0003_auto_20230529_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField(default=0)),
                ('descuento', models.IntegerField(default=0)),
                ('total_pagar', models.IntegerField(default=0)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto')),
            ],
            options={
                'verbose_name': 'Cotizacion',
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
        migrations.CreateModel(
            name='DetalleCotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizaciones.cotizacion')),
                ('materiales', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='materiales.material')),
            ],
            options={
                'verbose_name': 'DetalleCotizacion',
                'verbose_name_plural': 'DetalleCotizaciones',
            },
        ),
    ]