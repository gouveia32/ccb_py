from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    template_name = 'clientes/index.html'
    context = {
        'clientes': clientes
    }
    return render(request, template_name, context)

