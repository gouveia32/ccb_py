from django.db import models
from django.conf import settings
from django.utils import timezone

from ccb_py.core.mail import send_mail_template

class ClienteManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(nome__icontains=query) | \
            models.Q(contato_nome__icontains=query)
        )

class Cliente(models.Model):

    nome = models.CharField('Nome', max_length=120)
    contato_funcao = models.CharField('Função do Contato', blank=True, max_length=20)
    contato_nome = models.CharField('Nome do Contato', max_length=40)
    cgc_cpf = models.CharField('cgc/cpf', blank=True, max_length=18)
    incr_estadual = models.CharField('Inscrição Estadual', blank=True, max_length=20)
    cgc_cpf = models.CharField('cgc/cpf', blank=True, max_length=18)
    endereco = models.CharField('endereço', blank=True, max_length=100)
    cidade = models.CharField('cidade', blank=True, max_length=40)
    estado = models.CharField('uf', blank=True, max_length=2)
    cep = models.CharField('cep', blank=True, max_length=9)
    telefone1 = models.CharField('telefone1', max_length=20)
    telefone2 = models.CharField('telefone2', blank=True, max_length=20)
    telefone3 = models.CharField('telefone3', blank=True, max_length=20)
    email = models.EmailField('email', null=True, blank=True, max_length=60) 
    obs = models.TextField('Observação', blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = ClienteManager()

    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']
        