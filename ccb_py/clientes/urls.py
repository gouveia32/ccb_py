from django.urls import path, include

from ccb_py.clientes import views

app_name = 'clientes'
urlpatterns = [
    path('', views.index, 
        name='index'),    
]