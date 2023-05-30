# # models
# from .models import Cotizacion

# # django
# from django.contrib import admin

# from .models import Cotizacion, DetalleCotizacion

# class DetalleCotizacionAdmin(admin.ModelAdmin):
#     list_display = ('materiales', 'cantidad', 'total')
#     def total(self, obj):
#         return obj.total
#     total.short_description = 'Total'
    
# class DetalleCotizacionInline(admin.TabularInline):
#     model = DetalleCotizacion
#     fields = ('materiales', 'cantidad', 'get_total')
#     readonly_fields = ('get_total',)

#     def get_total(self, instance):
#         return instance.cantidad * instance.materiales.precio
#     get_total.short_description = 'Total'

# class CotizacionAdmin(admin.ModelAdmin):
#     inlines = [DetalleCotizacionInline]
#     fields = ('proyecto', 'subtotal', 'descuento', 'total_pagar')


# # Register your models here.
# admin.site.register(Cotizacion, CotizacionAdmin)
# admin.site.register(DetalleCotizacion, DetalleCotizacionAdmin)

from django.contrib import admin
from django.forms import ModelForm, TextInput
from django.urls import reverse_lazy
from django.utils.html import format_html
from .models import Cotizacion, DetalleCotizacion
from django.contrib.humanize.templatetags.humanize import intcomma

# class DetalleCotizacionForm(ModelForm):
#     class Meta:
#         model = DetalleCotizacion
#         fields = '__all__'
#         widgets = {
#             'cantidad': TextInput(attrs={'class': 'cantidad-input', })
        # }

class DetalleCotizacionInline(admin.TabularInline):
    model = DetalleCotizacion
    # form = DetalleCotizacionForm
    fields = ('materiales',
              'cantidad',
            #   'get_total'
              )
    extra = 1
    readonly_fields = ('get_total',)

    def get_total(self, instance):
        return instance.cantidad * instance.materiales.precio
    get_total.short_description = 'Total'


class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'subtotal_formatted', 'descuento', 'total_pagar_formatted')
    inlines = [DetalleCotizacionInline]
    fields = ('proyecto',
            #   'subtotal',
              'descuento',
            #   'total_pagar'
              )


    def total_pagar_formatted(self, obj):
        return intcomma(obj.total_pagar)
    total_pagar_formatted.short_description = 'total_pagar'
    
    def subtotal_formatted(self, obj):
        return intcomma(obj.subtotal)
    subtotal_formatted.short_description = 'subtotal'
    
    # class Media:
    #     js = ('admin/custom_scripts.js',)

admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(DetalleCotizacion)
