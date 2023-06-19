from django.contrib import admin
from .models import Cotizacion, DetalleCotizacion
from django.contrib.humanize.templatetags.humanize import intcomma
from import_export.admin import ImportExportModelAdmin  




class DetalleCotizacionInline(admin.TabularInline):
    model = DetalleCotizacion

    fields = ('materiales',
              'cantidad',
              )
    extra = 1
    readonly_fields = ('get_total',)

    def get_total(self, instance):
        return instance.cantidad * instance.materiales.precio
    get_total.short_description = 'Total'


class CotizacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('proyecto', 'subtotal_formatted', 'descuento', 'total_pagar_formatted', 'fecha_registro', 'fecha_actualizacion')
    search_fields = ['proyecto__nombre']
    inlines = [DetalleCotizacionInline]
    fields = ('proyecto',
              'descuento',
              )


    def total_pagar_formatted(self, obj):
        return intcomma(obj.total_pagar)
    total_pagar_formatted.short_description = 'total'
    
    def subtotal_formatted(self, obj):
        return intcomma(obj.subtotal)
    subtotal_formatted.short_description = 'subtotal'


admin.site.register(Cotizacion, CotizacionAdmin)

