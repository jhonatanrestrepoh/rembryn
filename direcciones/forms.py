# models
from .models import Direccion

# django
from django import forms

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ('direccion', 'departamento', 'municipio')
