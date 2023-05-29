# pytho
import re

# models
from clientes.models import Cliente
from django.core.exceptions import ValidationError

# aditional package
from smart_selects.db_fields import ChainedForeignKey

# django
from django.db import models


#Create your validations here.
def validate_direction(direccion):
    patterns = [
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}\s#\s\d{1,3}[a-zA-Z]?\-\d{1,3}\s(int)\s\d{1,4}$',
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}\s#\s\d{1,3}-\d{1,3}\s(Casa)\s\d$',
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}\s(sur)\s#\s\d{1,3}\s(sur)\s-\s\d{1,3}\s\d{1,2}$'
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}\s(sur)\s#\s\d{1,3}\s(sur)\s-\s\d{1,3}\s\d{1,2}\s(apto)\s\d{1,4}$',
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}[a-zA-Z]?\s(sur)\s#\s\d{1,3}\s(sur)\s-\s\d{1,3}\s\d{1,2}\s(apto)\s\d{1,4}$',
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}\s#\s\d{1,3}[a-zA-Z]?\-\d{1,3}(\s(int|apto)?\s?\d{1,4})?$',
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}\s(sur)\s#\s\d{1,3}(sur)-\d{1,3}\s\d{1,3}$',
        r'^(Calle|Carrera|Diagonal|Cl|Cr|Diag|Cra)\s\d{1,3}[a-zA-Z]?\s(sur)\s#\s\d{1,3}\s(sur)\s-\s\d{1,3}\s\d{1,2}\s(apto)\s\d{1,4}$',
        r'^Cra \d+ # \d+ [a-zA-Z] Sur \d+$',
        r'^Cra \d+[A-Z]? \d+-\d+$'
    ]
    
    is_valide = False
    for pattern in patterns:
        match = re.match(pattern, direccion, re.IGNORECASE)
        if match:
            is_valide = True
            break
    
    if not is_valide:
        raise ValidationError(
            _('Ingrese una dirección válida. Ej Cl 12 sur # 34C-56 Casa 2.'),
            code='invalid_direccion'
        )


# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(blank=False, max_length=100, unique=True)

class Municipio(models.Model):
    nombre = models.CharField(blank=False, max_length=100, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"


class Direccion(models.Model):
    direccion = models.CharField(unique=True, 
                                 blank=False, 
                                 max_length=100, 
                                 validators=[validate_direction], 
                                 error_messages={'unique': "La dirección ya existe. Ingresa una dirección diferente.",}
                                 )
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = ChainedForeignKey(Municipio,
                                  chained_field="departamento",
                                  chained_model_field="departamento",
                                  show_all=False,
                                  auto_choose=True,
                                  sort=True
                                  )


    def __str__(self):
        return self.direccion
    
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"