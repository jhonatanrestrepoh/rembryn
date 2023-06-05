# forms
from .forms import SignUpForm 

# django
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '🙂 Registrado con éxito ahora puedes ingresar a Rembryn')
            url = reverse('login')
            return redirect(url)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
