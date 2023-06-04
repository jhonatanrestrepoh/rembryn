# model
from .models import Cotizacion, DetalleCotizacion
from proyectos.models import Proyecto

# django
from django.urls import reverse
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def proyectos_cotizacion_view(request, id):
    try:
        cotizacion = Cotizacion.objects.select_related('proyecto').get(proyecto_id=id)
        detalles_cotizacion = DetalleCotizacion.objects.filter(cotizacion=cotizacion)
        print(cotizacion.subtotal)
        for detalle in detalles_cotizacion:
            print(detalle.materiales.nombre)
        
        return render(request, 'cotizaciones/cotizaciones_list.html', {'cotizacion': cotizacion,
                                                                       'detalles': detalles_cotizacion
                                                                       })
    except Cotizacion.DoesNotExist:
        # redirect a registrar el perfil
        proyecto = Proyecto.objects.get(id=id)
        messages.warning(request, f'El proyecto {proyecto.nombre} aún no tiene cotización')
        url = reverse('proyectos:list')
        return redirect(url)