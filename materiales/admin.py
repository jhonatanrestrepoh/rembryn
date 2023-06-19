# models
from .models import Material

# django
from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from import_export.admin import ImportExportModelAdmin  


class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'precio_formatted', 'fecha_registro', 'fecha_actualizacion')
    search_fields = ['nombre']
    def precio_formatted(self, obj):
        return intcomma(obj.precio)
    precio_formatted.short_description = 'Precio'


# Register your models here.
admin.site.register(Material, MaterialAdmin)
