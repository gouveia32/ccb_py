from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cliente
from .forms import ContactCliente

def index(request):
    clientes = Cliente.objects.all()
    template_name = 'clientes/index.html'
    context = {
        'clientes': clientes
    }
    return render(request, template_name, context)

def details(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    context = {}
    if request.method == 'POST':
        form = ContactCliente(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(cliente)
            form = ContactCliente()
    else:
        form = ContactCliente()
    context['form'] = form
    context['cliente'] = cliente
    template_name = 'clientes/details.html'
    return render(request, template_name, context)