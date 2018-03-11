from django.urls import path, include

from ccb_py.clientes import views

app_name = 'clientes'
urlpatterns = [
    path('', views.index, name='index'), 
    #path('<pk>/', views.details, name='details'), 
    path('<int:pk>/', views.details, name='details'),
]