from django.db import models
from clients.models import Client
from employees.models import Employee
from contractcategories.models import ContractCategory

class Contract(models.Model):
    """Mantem os dados de contracts alinhados ao dominio de contratos."""
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('ATIVO', 'Ativo'),
        ('VENCIDO', 'Vencido'),
        ('ENCERRADO', 'Encerrado'),
        ('CANCELADO', 'Cancelado'),
    ]

    number = models.CharField('NÃºmero', max_length=50, unique=True)
    title = models.CharField('TÃ­tulo', max_length=150)
    description = models.TextField('DescriÃ§Ã£o', max_length=500)
    start_date = models.DateField('Data de inÃ­cio')
    end_date = models.DateField('Data de fim')
    total_value = models.DecimalField('Valor total', max_digits=12, decimal_places=2, default=0)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='FuncionÃ¡rio responsÃ¡vel')
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
        """Retorna uma identificacao legivel do registro."""
        return f'{self.number} - {self.title}'
