from django.db import models
from contracts.models import Contract

class Notification(models.Model):
    """Mantem os dados de notifications alinhados ao dominio de contratos."""
    TYPE_CHOICES = [
        ('VENCIMENTO', 'Vencimento'),
        ('PAGAMENTO', 'Pagamento'),
        ('DOCUMENTO', 'Documento'),
        ('GERAL', 'Geral'),
    ]

    title = models.CharField('TÃ­tulo', max_length=150)
    message = models.TextField('Mensagem', max_length=500)
    notification_date = models.DateField('Data da notificaÃ§Ã£o')
    notification_type = models.CharField('Tipo de notificaÃ§Ã£o', max_length=20, choices=TYPE_CHOICES, default='GERAL')
    is_read = models.BooleanField('Lida', default=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='notifications', verbose_name='Contrato')

    class Meta:
        db_table = "gc_notification"
        verbose_name = 'NotificaÃ§Ã£o'
        verbose_name_plural = 'NotificaÃ§Ãµes'
        ordering = ['id']

    def mark_as_read(self):
        self.is_read = True
        self.save()
        return self.is_read

    def __str__(self):
        """Retorna uma identificacao legivel do registro."""
        return f'{self.title}'
