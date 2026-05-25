import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=150, verbose_name='Nome do arquivo')),
                ('file_type', models.CharField(max_length=50, verbose_name='Tipo do arquivo')),
                ('file_path', models.CharField(max_length=250, verbose_name='Caminho do arquivo')),
                ('upload_date', models.DateField(verbose_name='Data de upload')),
                ('is_signed', models.BooleanField(default=False, verbose_name='Assinado')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='gc_contracts.contract', verbose_name='Contrato')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'db_table': 'gc_document',
                'ordering': ['id'],
            },
        ),
    ]
