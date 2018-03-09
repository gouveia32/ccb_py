from django.contrib import admin

from .models import (Cliente)


class ClienteAdmin(admin.ModelAdmin):

    list_display = ['nome', 'contato_nome', 'telefone1', 'email']
    search_fields = ['nome', 'contato_nome']


admin.site.register(Cliente, ClienteAdmin)