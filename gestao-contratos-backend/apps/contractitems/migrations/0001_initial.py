import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_contracts', '0001_initial'),
        ('gc_services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantidade')),
                ('unitary_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preço unitário')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Preço total')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='gc_contracts.contract', verbose_name='Contrato')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_items', to='gc_services.service', verbose_name='Serviço')),
            ],
            options={
                'verbose_name': 'Item de contrato',
                'verbose_name_plural': 'Itens de contrato',
                'db_table': 'gc_contract_item',
                'ordering': ['id'],
            },
        ),
    ]
