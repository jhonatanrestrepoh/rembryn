# models
from .models import Cliente

# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'Cliente'

class CustomUserAdmin(UserAdmin):
    inlines = (ClienteInline,)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'celular', 'fecha_registro']
    search_fields = ['cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido']
    readonly_fields = ['cedula','fecha_registro', 'fecha_actualizacion']
    fieldsets = (
        ('Información Personal', {
            'fields': ('cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'celular')
        }),
        ('Fechas', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


