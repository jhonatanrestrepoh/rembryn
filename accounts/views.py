# django
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm


def login_view(request):
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
    url = reverse('accounts:login')
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


User = get_user_model()


def reset_password_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = user.pk
            reset_url = f"{request.scheme}://{request.get_host()}/reset_password_confirm/{uid}/{token}/"
            # Aquí puedes enviar el enlace de reset_url por correo electrónico
            print(reset_url)
            messages.success(request, 'Se ha enviado un correo electrónico con instrucciones para restablecer la contraseña.')
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})

@login_required
def reset_password_done(request):
    return render(request, 'registration/password_reset_done.html')

@login_required
def reset_password_confirm(request, uidb64, token):
    return PasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)

@login_required
def reset_password_complete(request):
    return render(request, 'registration/password_reset_complete.html')
