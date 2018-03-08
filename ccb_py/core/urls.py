from django.urls import path, include

from ccb_py.core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('contato/', views.contact, name = 'contact'),
]