from django.db import models

class ContractCategory(models.Model):
    """Mantem os dados de contractcategories alinhados ao dominio de contratos."""
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('DescriÃ§Ã£o', max_length=250)
    priority_level = models.IntegerField('NÃ­vel de prioridade', default=1)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        db_table = "gc_contract_category"
        verbose_name = 'Categoria de contrato'
        verbose_name_plural = 'Categorias de contrato'
        ordering = ['id']

    def __str__(self):
        """Retorna uma identificacao legivel do registro."""
        return f'{self.name}'
