# models
from clientes.models import Cliente
from direcciones.models import Direccion
# additional package
from smart_selects.db_fields import ChainedForeignKey 
# django
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


# Create your models here.
ESTADOS=(
    ('Pendiente', 'Pendiente'),
    ('Validado', 'Validado'),
    ('Cotizado', 'Cotizado'),
    ('Cancelado', 'Cancelado'),
    ('Terminado', 'Terminado'),
)


# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    descripcion = models.TextField(blank=True, max_length=500)
    fecha_fin = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    fecha_actualizacion =models.DateField(auto_now=True)
    fecha_registro =models.DateField(auto_now_add=True)
    estados = models.CharField(blank=False, null=False, max_length=100, choices=ESTADOS)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = ChainedForeignKey(Direccion,
                                  chained_field='cliente',
                                  chained_model_field='cliente',
                                  show_all=False,
                                  auto_choose=True,
                                  sort=True
                                  )

    def __str__(self):
        return self.nombre