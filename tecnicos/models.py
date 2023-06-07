# django
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


#Create your validations here.
def validate_cedula(value):
    if not value.isdigit():
        raise ValidationError(
            _('La cédula debe contener solo números.'),
            code='invalid_format'
        )
    if len(value) < 5 or len(value) > 10:
        raise ValidationError(
            _('La cédula debe tener entre 5 y 10 dígitos.'),
            code='invalid_length'
        )
    

def validate_not_contain_numbers(value):
    if any(char.isdigit() for char in value):
        raise ValidationError(
            _('Este campo no puede contener números.'),
            code='invalid_nombre'
        )


def validate_celular(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError(
            _('El número de celular debe tener 10 dígitos y ser numérico.'),
            code='invalid_celular'
        )


# Create your models here.

class Tecnico(models.Model):
    cedula = models.CharField(unique=True,
                              blank=False,
                              max_length=10,
                              verbose_name = 'Cédula',
                              validators=[validate_cedula],
                              error_messages={'unique': 'Ya existe un usuario con esta cédula'}
                              )
    
    primer_nombre = models.CharField(blank=False,
                                     max_length=50,
                                     validators=[validate_not_contain_numbers]
                                     )
    
    segundo_nombre = models.CharField(blank=True,
                                      max_length=50,
                                      validators=[validate_not_contain_numbers]
                                      )
    
    primer_apellido = models.CharField(blank=False,
                                       max_length=50,
                                       validators=[validate_not_contain_numbers]
                                       )
    
    segundo_apellido = models.CharField(blank=True,
                                        max_length=50,
                                        validators=[validate_not_contain_numbers]
                                        )
    
    celular = models.CharField(blank=False,
                               max_length=10,
                               validators=[validate_celular]
                               )
    
    fecha_registro = models.DateField(auto_now_add=True)
    
    fecha_actualizacion = models.DateField(auto_now=True)
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"
    
    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"