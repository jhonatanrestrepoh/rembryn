from django.urls import path
from . import views

app_name= 'proyectos'

urlpatterns = [
    path('proyectos/', views.proyectos_list_view, name='list'),
]