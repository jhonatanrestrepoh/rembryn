# models
from .models import Proyecto
from visitas_tecnicas.models import VisitaTecnica

# django
from django.contrib import admin

class VisitaTecnicaInline(admin.TabularInline):
    model = VisitaTecnica
    extra = 1
    
class ProyectoAdmin(admin.ModelAdmin):
    inlines = [VisitaTecnicaInline]

# Register your models here.
admin.site.register(Proyecto, ProyectoAdmin)
