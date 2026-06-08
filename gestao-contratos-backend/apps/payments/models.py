from django.db import models
from contracts.models import Contract

class Payment(models.Model):
    """Mantem os dados de payments alinhados ao dominio de contratos."""
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('ATRASADO', 'Atrasado'),
        ('CANCELADO', 'Cancelado'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('PIX', 'Pix'),
        ('BOLETO', 'Boleto'),
        ('CARTAO', 'CartÃ£o'),
        ('TRANSFERENCIA', 'TransferÃªncia'),
        ('DINHEIRO', 'Dinheiro'),
    ]

    installment_number = models.IntegerField('NÃºmero da parcela', default=1)
    due_date = models.DateField('Data de vencimento')
    payment_date = models.DateField('Data de pagamento', null=True, blank=True)
    value = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    payment_method = models.CharField('Forma de pagamento', max_length=20, choices=PAYMENT_METHOD_CHOICES, default='PIX')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='payments', verbose_name='Contrato')

    class Meta:
        db_table = "gc_payment"
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id']

    def mark_as_paid(self, payment_date):
        self.payment_date = payment_date
        self.status = 'PAGO'
        self.save()
        return self.status

    def __str__(self):
        """Retorna uma identificacao legivel do registro."""
        return f'Parcela {self.installment_number} - {self.contract.number}'
