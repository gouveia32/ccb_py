from django.urls import path, include

from django.contrib.auth import views
from .views import register
from .views import dashboard
from .views import edit
from .views import edit_password
from .views import password_reset

app_name = 'accounts'
urlpatterns = [
    path('', dashboard, 
        name='dashboard'),
    path('entrar/', views.login, 
        {'template_name': 'accounts/login.html'}, name='login'),
    path('sair/', views.logout, {'next_page': 'core:home'}, name='logout'),
    path('cadatre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password, name='edit_password'),
]
