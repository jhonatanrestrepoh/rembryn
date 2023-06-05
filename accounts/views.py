# django
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect



from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('login')
            return redirect(url)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
