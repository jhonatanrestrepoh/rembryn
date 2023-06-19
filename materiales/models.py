
# django
from django.db import models
from django.core.exceptions import ValidationError


# Create your validations here.
def validate_valor(value):
    if not (1 <= value < 10_000_000):
        raise ValidationError("El precio debe ser mayor a 1.00 y menor a 10,000,000.00")


# Create your models here.
class Material(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2, validators=[validate_valor])
    fecha_actualizacion= models.DateField(auto_now=True)
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"