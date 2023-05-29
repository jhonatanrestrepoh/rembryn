# models
from .models import Material

# django
from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_formatted')

    def precio_formatted(self, obj):
        return intcomma(obj.precio)
    precio_formatted.short_description = 'Precio'


# Register your models here.
admin.site.register(Material, MaterialAdmin)
