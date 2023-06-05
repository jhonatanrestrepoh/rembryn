# views
from . import views

# django
from django.urls import path

app_name = 'direcciones'

urlpatterns = [
    path('crear/', views.crear_view, name='crear'),
    path('direccion/edit/<int:pk>/', views.edit_view, name='editar'),
    path('direccion/delete/<int:pk>/', views.delete_view, name='borrar'),
    path('direcciones/', views.direcciones_view, name='direcciones'),
]
