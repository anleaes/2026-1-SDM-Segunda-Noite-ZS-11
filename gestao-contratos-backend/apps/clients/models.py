from django.db import models
from persons.models import Person
from contactchannels.models import ContactChannel

class Client(Person):
    CLIENT_TYPE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, unique=True)
    company_name = models.CharField('Razão social/Nome fantasia', max_length=150)
    client_type = models.CharField('Tipo de cliente', max_length=2, choices=CLIENT_TYPE_CHOICES)
    is_active = models.BooleanField('Ativo', default=True)
    contact_channels = models.ManyToManyField(ContactChannel, verbose_name='Canais de contato', blank=True)

    class Meta:
        db_table = "gc_client"
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return f'{self.company_name} - {self.cpf_cnpj}'
