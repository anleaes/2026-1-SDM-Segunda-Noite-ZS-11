from django.db import models

class Person(models.Model):
    """Mantem os dados de persons alinhados ao dominio de contratos."""
    first_name = models.CharField('Primeiro nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    address = models.CharField('EndereÃ§o', max_length=150)
    phone = models.CharField('Telefone', max_length=30)
    email = models.EmailField('Email', max_length=100)

    class Meta:
        db_table = "gc_person"
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
