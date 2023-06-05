# models
from .models import Cliente

# django
from django import forms

class ClienteForm(forms.ModelForm):
   
    class Meta:
        model = Cliente
        fields = ['cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'celular']
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control bg-secondary text-white', 'placeholder': 'Ingrese la cédula', 'maxlength': '10'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control bg-secondary text-white', 'placeholder': 'Ingrese el primer nombre', 'maxlength': '50'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control bg-secondary text-white', 'placeholder': 'Ingrese el segundo nombre', 'maxlength': '50'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control bg-secondary text-white', 'placeholder': 'Ingrese el primer apellido', 'maxlength': '50'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control bg-secondary text-white', 'placeholder': 'Ingrese el segundo apellido', 'maxlength': '50'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control bg-secondary text-white', 'placeholder': 'Ingrese el número de celular', 'maxlength': '10'}),
        }