from django.db import models
from clients.models import Client
from employees.models import Employee
from contractcategories.models import ContractCategory

class Contract(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('ATIVO', 'Ativo'),
        ('VENCIDO', 'Vencido'),
        ('ENCERRADO', 'Encerrado'),
        ('CANCELADO', 'Cancelado'),
    ]

    number = models.CharField('Número', max_length=50, unique=True)
    title = models.CharField('Título', max_length=150)
    description = models.TextField('Descrição', max_length=500)
    start_date = models.DateField('Data de início')
    end_date = models.DateField('Data de fim')
    total_value = models.DecimalField('Valor total', max_digits=12, decimal_places=2, default=0)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Funcionário responsável')
    category = models.ForeignKey(ContractCategory, on_delete=models.CASCADE, verbose_name='Categoria')

    class Meta:
        db_table = "gc_contract"
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['id']

    def update_status(self, new_status):
        self.status = new_status
        self.save()
        return self.status

    def __str__(self):
        return f'{self.number} - {self.title}'
