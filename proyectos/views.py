# model
from clientes.models import Cliente
from direcciones.models import Direccion
from cotizaciones.models import Cotizacion

# django
from django.urls import reverse
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.db.models import Max, F, Exists, OuterRef
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def proyectos_list_view(request):
    
    cliente = request.user.cliente 
    
    if cliente:
        direcciones = Direccion.objects.filter(cliente=cliente)
        
        if direcciones.exists():
            proyectos = cliente.proyecto_set.annotate(
                    ultima_fecha_visita=Max('visitatecnica__fecha_visita'),
                    nombre_tecnico=F('visitatecnica__tecnico__primer_nombre'),
                    apellido_tecnico=F('visitatecnica__tecnico__primer_apellido'),
                    tiene_cotizacion=Exists(Cotizacion.objects.filter(proyecto=OuterRef('pk')))
                    
                ).values('id', 'nombre', 'direccion__direccion', 'ultima_fecha_visita', 'nombre_tecnico', 'apellido_tecnico', 'tiene_cotizacion')
            return render(request, 'proyectos/proyectos_list.html', {'proyectos': proyectos})
        
        else:
            messages.warning(request, '😳 ¡Ups! Primero debes registrar una dirección')
            url = reverse('direcciones:crear')
            return redirect(url)
    else:
        messages.warning(request, '😳 ¡Ups! Primero debes completar tu información personal')
        url = reverse('clientes:perfil')
        return redirect(url)
