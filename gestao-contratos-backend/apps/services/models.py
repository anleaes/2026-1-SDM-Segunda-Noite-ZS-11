from django.db import models

class Service(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=250)
    unit_price = models.DecimalField('Preço unitário', max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        db_table = "gc_service"
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
