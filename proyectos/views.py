# model
from clientes.models import Cliente

# django
from django.urls import reverse
from django.contrib import messages 
from django.db.models import Max, F
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def proyectos_list_view(request):
    try:
        cliente = request.user.cliente  # Suponiendo que el modelo de cliente se asocia al usuario mediante un campo OneToOneField
        proyectos = cliente.proyecto_set.annotate(
                ultima_fecha_visita=Max('visitatecnica__fecha_visita'),
                nombre_tecnico=F('visitatecnica__tecnico__primer_nombre'),
                apellido_tecnico=F('visitatecnica__tecnico__primer_apellido')
                
            ).values('id', 'nombre', 'direccion__direccion', 'ultima_fecha_visita', 'nombre_tecnico', 'apellido_tecnico')
        return render(request, 'proyectos/proyectos_list.html', {'proyectos': proyectos})
    except Cliente.DoesNotExist:
        # redirect a registrar el perfil
        messages.warning(request, '😳 ¡Ups! Primero debes completar tu información personal')
        url = reverse('clientes:perfil')
        return redirect(url)