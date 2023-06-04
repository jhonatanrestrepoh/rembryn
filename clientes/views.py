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
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, instance=cliente)
        if cliente_form.is_valid():
            cliente = cliente_form.save()
            messages.success(request, 'Se actualizó tu perfil')
            return redirect(reverse('clientes:perfil'))
    else:
        try: 
            cliente = Cliente.objects.get(usuario=user_id)  
            cliente_form = ClienteForm(instance=cliente)
        
            Direccion.objects.get(cliente_id=cliente.id)
        except Exception:
            context = {
                'cliente_form': ClienteForm(),
                'direccion_button': True
            }
            return render(request, 'clientes/perfil.html', context)
        else:        
            context = {
                'cliente_form': cliente_form,
                'direccion_button': False
            }
            return render(request, 'clientes/perfil.html', context)