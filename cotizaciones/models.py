#models
from proyectos.models import Proyecto
from materiales.models import Material

# django
from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Cotizacion(models.Model):
    subtotal = models.IntegerField(default=0)
    descuento = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(15)])
    total_pagar = models.IntegerField(default=0)
    fecha_actualizacion = models.DateField(auto_now=True)
    fecha_registro = models.DateField(auto_now_add=True)
    proyecto = models.OneToOneField(Proyecto,
                                    on_delete=models.CASCADE,
                                    error_messages={'unique':'Ya existe una cotización para este proyecto.'}
                                    )

    
    def save(self, *args, **kwargs):
        descuento_int = self.subtotal * (self.descuento / 100)
        self.total_pagar = self.subtotal - descuento_int
        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(self.proyecto)   

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"

class DetalleCotizacion(models.Model):
    cantidad = models.PositiveSmallIntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(1)])
    total_pagar = models.IntegerField(blank=True, null=True)
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    materiales = models.ForeignKey(Material, blank=False, on_delete=models.CASCADE,)

    
    def save(self, *args, **kwargs):
        self.total_pagar = int(self.cantidad) * int(self.materiales.precio)
        super().save(*args, **kwargs)
        subtotal = self.cotizacion.detallecotizacion_set.aggregate(total_sum=Sum('total_pagar'))['total_sum']
        self.cotizacion.subtotal = subtotal if subtotal is not None else 0
        self.cotizacion.save()

    class Meta:
        verbose_name = "Detalle de cotización"
        verbose_name_plural = "Detalle de cotizaciones"