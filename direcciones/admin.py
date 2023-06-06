# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# models
from .models import Direccion, Departamento, Municipio

@admin.register(Municipio)
class MunicipioAdmin(ImportExportModelAdmin):
    pass

@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Direccion)


