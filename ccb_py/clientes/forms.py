from django import forms
from django.core.mail import send_mail
from django.conf import settings

from ccb_py.core.mail import send_mail_template


class ContactCliente(forms.Form):
    
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    def send_mail(self, cliente):
        subject = '[%s] Contato' % cliente
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'clientes/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )


