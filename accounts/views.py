# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login_view(request):
    print('dentro de login view')
    if request.method == 'POST':
        print('dentro de post')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print('dentro de if')
            
            login(request, user)
            return redirect('proyectos:list')  # Redirige a la página de inicio después de iniciar sesión correctamente
        else:
            print('dentro de eñse')
            error_message = 'Nombre de usuario o contraseña incorrectos'
            return render(request, 'registration/login.html', {'error_message': error_message})
    
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    url = reverse('account:login')
    return redirect(url)


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu contraseña ha sido cambiada correctamente.')
            return redirect('perfil')  # Reemplaza 'perfil' con el nombre de la URL a la que quieres redirigir después de cambiar la contraseña
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})
