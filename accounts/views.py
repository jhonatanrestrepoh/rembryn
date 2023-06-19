
# django
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
# forms
from .forms import SignUpForm 



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '🙂 Registrado con éxito ahora puedes ingresar a Rembryn')
            url = reverse('login')
            return redirect(url)
    else:
        initial_data = {'username': request.GET.get('username', ''), 'email': request.GET.get('email', '')}
        form = SignUpForm(initial=initial_data)
    return render(request, 'registration/signup.html', {'form': form})
