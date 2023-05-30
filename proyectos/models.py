# models
from clientes.models import Cliente
from direcciones.models import Direccion
from tecnicos.models import Tecnico

# additional package
from smart_selects.db_fields import ChainedForeignKey 

# django
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


# Create your models here.
ESTADOS=(
    ('Pendiente', 'Pendiente'),
    ('Validado', 'Validado'),
    ('Cotizado', 'Cotizado'),
    ('Cancelado', 'Cancelado'),
    ('Terminado', 'Terminado'),
)

# Create your validations here.
min_date = timezone.now().date().strftime('%d-%m-%Y')
validators = [MinValueValidator(timezone.now().date(), message=f"La fecha debe ser igual o posterior a {min_date}.")]

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    descripcion = models.TextField(blank=True, max_length=500)
    fecha_fin = models.DateField(
                                #  validators=validators 
                                )
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
    def clean(self):
        if not self._state.adding:  # Verificar si se está modificando un objeto existente
            return  # No realizar validación si se está modificando un objeto existente

        if self.fecha_fin < timezone.now().date():
            raise ValidationError(f'La fecha debe ser igual o posterior a la fecha actual {min_date}.')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    