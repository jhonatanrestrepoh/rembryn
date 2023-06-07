# models
from proyectos.models import Proyecto
from tecnicos.models import Tecnico

# django
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# Create your validations here.
min_date = timezone.now().date().strftime('%d-%m-%Y')

# Create your models here.
class VisitaTecnica(models.Model):
    fecha_visita =models.DateField(blank=False,)
    tecnico = models.ForeignKey(Tecnico, blank=False, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, blank=False, on_delete=models.CASCADE)
    fecha_actualizacion= models.DateField(auto_now=True)
    fecha_registro= models.DateField(auto_now_add=True)
    descripcion = models.TextField(blank=True, max_length=500)
    
    def clean(self):
        if not self._state.adding:  # Verificar si se está modificando un objeto existente
            return  # No realizar validación si se está modificando un objeto existente

        if self.fecha_visita < timezone.now().date():
            raise ValidationError(f'La fecha debe ser igual o posterior a la fecha actual {min_date}.')

    def __str__(self):
        return f"{self.id} {self.proyecto.nombre} "
    
    class Meta:
        verbose_name = "Visita técnica"
        verbose_name_plural = "Visitas técnicas"