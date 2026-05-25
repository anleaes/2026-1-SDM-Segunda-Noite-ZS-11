from django.db import models

class ContactChannel(models.Model):
    CHANNEL_CHOICES = [
        ('EMAIL', 'Email'),
        ('TELEFONE', 'Telefone'),
        ('WHATSAPP', 'WhatsApp'),
        ('OUTRO', 'Outro'),
    ]

    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=250)
    channel_type = models.CharField('Tipo de canal', max_length=20, choices=CHANNEL_CHOICES)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        db_table = "gc_contract_channel"
        verbose_name = 'Canal de contato'
        verbose_name_plural = 'Canais de contato'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.channel_type}'
