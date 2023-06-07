# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# models
from .models import Direccion, Departamento, Municipio

class BaseAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    
# @admin.register(Municipio)
# class MunicipioAdmin(BaseAdmin, ImportExportModelAdmin):
#     pass

# @admin.register(Departamento)
# class DepartamentoAdmin(BaseAdmin, ImportExportModelAdmin):
#     pass


@admin.register(Direccion)
class DepartamentoAdmin(BaseAdmin):
    search_fields =['cliente__primer_nombre','cliente__segundo_nombre', 'cliente__primer_apellido', 'cliente__segundo_apellido', 'direccion']
    
    list_display = ['get_primer_nombre_cliente', 'direccion', 'get_departamento', 'get_municipio', 'fecha_registro']
    
    def get_primer_nombre_cliente(self, obj):
        primer_nombre= obj.cliente.primer_nombre
        segundo_nombre= obj.cliente.segundo_nombre
        primer_apellido= obj.cliente.primer_apellido
        segundo_apellido= obj.cliente.segundo_apellido
        return f'{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}'
    get_primer_nombre_cliente.short_description = 'Cliente'

    def get_departamento(self, obj):
        return obj.departamento.nombre
    get_departamento.short_description = 'Departamento'
    
    def get_municipio(self, obj):
        return obj.municipio.nombre
    get_municipio.short_description = 'Municipio'

