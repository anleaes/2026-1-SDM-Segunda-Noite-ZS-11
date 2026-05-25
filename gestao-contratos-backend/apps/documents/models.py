from django.db import models
from contracts.models import Contract

class Document(models.Model):
    file_name = models.CharField('Nome do arquivo', max_length=150)
    file_type = models.CharField('Tipo do arquivo', max_length=50)
    file_path = models.CharField('Caminho do arquivo', max_length=250)
    upload_date = models.DateField('Data de upload')
    is_signed = models.BooleanField('Assinado', default=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='documents', verbose_name='Contrato')

    class Meta:
        db_table = "gc_document"
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['id']

    def sign_document(self):
        self.is_signed = True
        self.save()
        return self.is_signed

    def __str__(self):
        return f'{self.file_name}'
