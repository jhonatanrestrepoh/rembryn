# models
from .models import Proyecto
from visitas_tecnicas.models import VisitaTecnica

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  


class VisitaTecnicaAdmin(admin.ModelAdmin):
    pass

class VisitaTecnicaInline(admin.TabularInline):
    model = VisitaTecnica
    extra = 1
    
class ProyectoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [VisitaTecnicaInline]

# Register your models here.
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(VisitaTecnica, VisitaTecnicaAdmin)
