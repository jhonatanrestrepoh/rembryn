# forms
from .forms import ClienteForm

# model
from .models import Cliente
from direcciones.models import Direccion

# django
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def perfil_view(request):
    user_id = request.user.id
    try:
        cliente = Cliente.objects.get(usuario_id=user_id)
        is_new_cliente = False
    except Cliente.DoesNotExist:
        cliente = Cliente(usuario_id=user_id)
        is_new_cliente = True

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, instance=cliente)
        if cliente_form.is_valid():
            cliente = cliente_form.save()
            if is_new_cliente:
                messages.success(request, 'Se creó tu perfil')
            else:
                messages.success(request, 'Se actualizó tu perfil')
            return redirect(reverse('clientes:perfil'))
    else:
        cliente_form = ClienteForm(instance=cliente)
        
    context = {
        'cliente_form': cliente_form,
        'is_new_cliente': is_new_cliente
    }
    return render(request, 'clientes/perfil.html', context)
