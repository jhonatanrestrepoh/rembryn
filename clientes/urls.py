# views
from . import views

# django
from django.urls import path

app_name= 'clientes'

urlpatterns = [
    path('perfil/', views.perfil_view, name='perfil'),
]