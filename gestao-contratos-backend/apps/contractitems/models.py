from django.db import models
from contracts.models import Contract
from services.models import Service

class ContractItem(models.Model):
    quantity = models.IntegerField('Quantidade', default=1)
    unitary_price = models.DecimalField('Preço unitário', max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField('Preço total', max_digits=12, decimal_places=2, default=0)
    description = models.TextField('Descrição', max_length=250)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='contract_items', verbose_name='Serviço')
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
        return f'{self.contract.number} - {self.service.name}'
