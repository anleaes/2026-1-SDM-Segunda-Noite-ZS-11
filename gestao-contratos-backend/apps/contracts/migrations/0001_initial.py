import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_clients', '0001_initial'),
        ('gc_contractcaregories', '0001_initial'),
        ('gc_employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, unique=True, verbose_name='Número')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('start_date', models.DateField(verbose_name='Data de início')),
                ('end_date', models.DateField(verbose_name='Data de fim')),
                ('total_value', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Valor total')),
                ('status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('ATIVO', 'Ativo'), ('VENCIDO', 'Vencido'), ('ENCERRADO', 'Encerrado'), ('CANCELADO', 'Cancelado')], default='PENDENTE', max_length=20, verbose_name='Status')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gc_contractcaregories.contractcategory', verbose_name='Categoria')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gc_clients.client', verbose_name='Cliente')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gc_employees.employee', verbose_name='Funcionário responsável')),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
                'db_table': 'gc_contract',
                'ordering': ['id'],
            },
        ),
    ]
