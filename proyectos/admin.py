from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Proyecto
from visitas_tecnicas.models import VisitaTecnica

class VisitaTecnicaInline(admin.TabularInline):
    model = VisitaTecnica
    extra = 1

    def delete_link(self, obj):
        if obj.id:
            url = reverse('admin:visitas_tecnicas_visitatecnica_delete', args=[obj.id])
            return format_html('<a href="{}" class="button">Eliminar</a>', url)
        return ''
    delete_link.short_description = 'Eliminar'

    fields = ('fecha_visita', 'tecnico', 'delete_link')
    readonly_fields = ('delete_link',)
    can_delete = False

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cliente', 'direccion', 'estado', 'fecha_registro', 'fecha_actualizacion')
    search_fields = ['nombre', 'direccion', 'cliente']
    inlines = [VisitaTecnicaInline]

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(VisitaTecnica)
