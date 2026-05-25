from django.db import models
from useraccounts.models import UserAccount
from contracts.models import Contract

class Audit(models.Model):
    action = models.CharField('Ação', max_length=100)
    description = models.TextField('Descrição', max_length=500)
    action_date = models.DateField('Data da ação')
    ip_address = models.CharField('Endereço IP', max_length=50)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='audits', verbose_name='Usuário')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='audits', verbose_name='Contrato')

    class Meta:
        db_table = "gc_audit"
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditorias'
        ordering = ['id']

    def __str__(self):
        return f'{self.action} - {self.contract.number}'
