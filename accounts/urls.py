# views
from . import views

# django
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password_view, name='change_password'),
    path('reset_password/', views.reset_password_view, name='reset_password'),
    path('reset_password_done/', views.reset_password_done, name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', views.reset_password_confirm, name='password_reset_confirm'),
    path('reset_password_complete/', views.reset_password_complete, name='password_reset_complete'),
    
]