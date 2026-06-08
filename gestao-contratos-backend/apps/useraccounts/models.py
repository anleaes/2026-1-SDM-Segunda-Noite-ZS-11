from django.db import models
from employees.models import Employee

class UserAccount(models.Model):
    """Mantem os dados de useraccounts alinhados ao dominio de contratos."""
    PROFILE_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('GERENTE', 'Gerente'),
        ('OPERADOR', 'Operador'),
    ]

    username = models.CharField('UsuÃ¡rio', max_length=100, unique=True)
    password = models.CharField('Senha', max_length=100)
    profile = models.CharField('Perfil', max_length=20, choices=PROFILE_CHOICES)
    is_active = models.BooleanField('Ativo', default=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='FuncionÃ¡rio')

    class Meta:
        db_table = "gc_user_account"
        verbose_name = 'UsuÃ¡rio'
        verbose_name_plural = 'UsuÃ¡rios'
        ordering = ['id']

    def __str__(self):
        return f'{self.username} - {self.profile}'
