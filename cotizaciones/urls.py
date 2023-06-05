# views
from . import views

# django
from django.urls import path

app_name= 'cotizaciones'

urlpatterns = [
    path('cotizacion/<int:id>/', views.proyectos_cotizacion_view, name='cotizacion'),
]