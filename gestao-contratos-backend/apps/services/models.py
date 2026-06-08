from django.db import models

class Service(models.Model):
    """Mantem os dados de services alinhados ao dominio de contratos."""
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('DescriÃ§Ã£o', max_length=250)
    unit_price = models.DecimalField('PreÃ§o unitÃ¡rio', max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        db_table = "gc_service"
        verbose_name = 'ServiÃ§o'
        verbose_name_plural = 'ServiÃ§os'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
