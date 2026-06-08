from django.db import models
from contracts.models import Contract
from services.models import Service

class ContractItem(models.Model):
    """Mantem os dados de contractitems alinhados ao dominio de contratos."""
    quantity = models.IntegerField('Quantidade', default=1)
    unitary_price = models.DecimalField('PreÃ§o unitÃ¡rio', max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField('PreÃ§o total', max_digits=12, decimal_places=2, default=0)
    description = models.TextField('DescriÃ§Ã£o', max_length=250)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='contract_items', verbose_name='ServiÃ§o')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='items', verbose_name='Contrato')

    class Meta:
        db_table = "gc_contract_item"
        verbose_name = 'Item de contrato'
        verbose_name_plural = 'Itens de contrato'
        ordering = ['id']

    def calculate_total_price(self):
        self.total_price = self.quantity * self.unitary_price
        self.save()
        return self.total_price

    def __str__(self):
        """Retorna uma identificacao legivel do registro."""
        return f'{self.contract.number} - {self.service.name}'
