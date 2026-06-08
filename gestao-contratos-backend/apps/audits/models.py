from django.db import models
from useraccounts.models import UserAccount
from contracts.models import Contract

class Audit(models.Model):
    """Mantem os dados de audits alinhados ao dominio de contratos."""
    action = models.CharField('AÃ§Ã£o', max_length=100)
    description = models.TextField('DescriÃ§Ã£o', max_length=500)
    action_date = models.DateField('Data da aÃ§Ã£o')
    ip_address = models.CharField('EndereÃ§o IP', max_length=50)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='audits', verbose_name='UsuÃ¡rio')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='audits', verbose_name='Contrato')

    class Meta:
        db_table = "gc_audit"
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditorias'
        ordering = ['id']

    def __str__(self):
        """Retorna uma identificacao legivel do registro."""
        return f'{self.action} - {self.contract.number}'
