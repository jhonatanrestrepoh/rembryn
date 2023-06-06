# forms
from .forms import DireccionForm

# models
from .models import Direccion
from clientes.models import Cliente

# django
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

DIRECCIONES = 'direcciones:direcciones'


# Create your views here.

@login_required
def crear_view(request):
    try:
        cliente = Cliente.objects.get(usuario=request.user.id)
        if request.method == 'POST':
            form = DireccionForm(request.POST)
            if form.is_valid():
                direccion = form.save(commit=False)
                direccion.cliente_id = cliente.id  # Asignar el ID del cliente
                direccion.save()
                messages.success(request, 'Dirección guardada con éxito')
                return redirect('direcciones:direcciones')
        else:
            form = DireccionForm(initial={'cliente': cliente.id})  # Pasar el ID del cliente al formulario

        return render(request, 'direcciones/crear.html', {'form': form})
    except ObjectDoesNotExist:
        messages.warning(request, '😳 ¡Ups! Primero debes completar tu información personal')
        url = reverse('proyectos:list')
        return redirect(url)


@login_required
def edit_view(request, pk):
    direccion = get_object_or_404(Direccion, pk=pk)
    if request.method == 'POST':
        form = DireccionForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dirección actualizada con éxito')
            url = reverse('direcciones:direcciones')
            return redirect(url)  # Redirecciona a la lista de direcciones después de actualizar
    else:
        form = DireccionForm(instance=direccion)
    
    return render(request, 'direcciones/editar.html', {'form': form})


@login_required
def delete_view(request, pk):
    direccion = get_object_or_404(Direccion, pk=pk)
    if request.method == 'POST':
        direccion.delete()
        return redirect(DIRECCIONES)


@login_required
def direcciones_view(request):
    try:
        cliente = request.user.cliente
        direcciones = cliente.direccion_set.all()
       
        return render(request, 'direcciones/direcciones.html', {'direcciones': direcciones})
    
    except ObjectDoesNotExist:
        messages.warning(request, '😳 ¡Ups! Primero debes completar tu información personal')
        url = reverse('proyectos:list')
        return redirect(url)