# models
from .models import Proyecto

# django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required
def proyectos_list_view(request):
    try:
        cliente = request.user.cliente  # Suponiendo que el modelo de cliente se asocia al usuario mediante un campo OneToOneField
        proyectos = cliente.proyecto_set.all()  # Obtener todos los proyectos asociados al cliente
        return render(request, 'proyectos/proyectos_list.html', {'proyectos': proyectos})
    except Exception:
        # redirect a registrar el perfil
        return render(request, 'proyectos/proyectos_list.html', {})
