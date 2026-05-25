from django.db import models
from contracts.models import Contract

class Notification(models.Model):
    TYPE_CHOICES = [
        ('VENCIMENTO', 'Vencimento'),
        ('PAGAMENTO', 'Pagamento'),
        ('DOCUMENTO', 'Documento'),
        ('GERAL', 'Geral'),
    ]

    title = models.CharField('Título', max_length=150)
    message = models.TextField('Mensagem', max_length=500)
    notification_date = models.DateField('Data da notificação')
    notification_type = models.CharField('Tipo de notificação', max_length=20, choices=TYPE_CHOICES, default='GERAL')
    is_read = models.BooleanField('Lida', default=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='notifications', verbose_name='Contrato')

    class Meta:
        db_table = "gc_notification"
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['id']

    def mark_as_read(self):
        self.is_read = True
        self.save()
        return self.is_read

    def __str__(self):
        return f'{self.title}'
