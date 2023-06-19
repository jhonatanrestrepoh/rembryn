# models
from .models import Tecnico

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  


@admin.register(Tecnico)
class TecnicoAdmin(ImportExportModelAdmin):
    list_display = ['cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'celular', 'fecha_registro']
    search_fields = ['cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido']

