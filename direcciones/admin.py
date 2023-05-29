# models
from .models import Direccion, Departamento, Municipio

# django
from django.contrib import admin


# Register your models here.
admin.site.register(Direccion)
admin.site.register(Departamento)
admin.site.register(Municipio)

