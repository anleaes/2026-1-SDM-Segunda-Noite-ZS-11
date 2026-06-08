from django.db import models
from persons.models import Person

class Employee(Person):
    """Mantem os dados de employees alinhados ao dominio de contratos."""
    registration = models.CharField('MatrÃ­cula', max_length=30, unique=True)
    position = models.CharField('Cargo', max_length=100)
    department = models.CharField('Departamento', max_length=100)
    salary = models.DecimalField('SalÃ¡rio', max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = "gc_employee"
        verbose_name = 'FuncionÃ¡rio'
        verbose_name_plural = 'FuncionÃ¡rios'
        ordering = ['id']

    def __str__(self):
        """Retorna uma identificacao legivel do registro."""
        return f'{self.first_name} {self.last_name} - {self.position}'
