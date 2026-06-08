from django.db import models
from persons.models import Person
from contactchannels.models import ContactChannel

class Client(Person):
    """Mantem os dados de clients alinhados ao dominio de contratos."""
    CLIENT_TYPE_CHOICES = [
        ('PF', 'Pessoa FÃ­sica'),
        ('PJ', 'Pessoa JurÃ­dica'),
    ]

    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, unique=True)
    company_name = models.CharField('RazÃ£o social/Nome fantasia', max_length=150)
    client_type = models.CharField('Tipo de cliente', max_length=2, choices=CLIENT_TYPE_CHOICES)
    is_active = models.BooleanField('Ativo', default=True)
    contact_channels = models.ManyToManyField(ContactChannel, verbose_name='Canais de contato', blank=True)

    class Meta:
        db_table = "gc_client"
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        """Retorna uma identificacao legivel do registro."""
        return f'{self.company_name} - {self.cpf_cnpj}'
