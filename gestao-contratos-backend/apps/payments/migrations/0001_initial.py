import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment_number', models.IntegerField(default=1, verbose_name='Número da parcela')),
                ('due_date', models.DateField(verbose_name='Data de vencimento')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Data de pagamento')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor')),
                ('status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('PAGO', 'Pago'), ('ATRASADO', 'Atrasado'), ('CANCELADO', 'Cancelado')], default='PENDENTE', max_length=20, verbose_name='Status')),
                ('payment_method', models.CharField(choices=[('PIX', 'Pix'), ('BOLETO', 'Boleto'), ('CARTAO', 'Cartão'), ('TRANSFERENCIA', 'Transferência'), ('DINHEIRO', 'Dinheiro')], default='PIX', max_length=20, verbose_name='Forma de pagamento')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='gc_contracts.contract', verbose_name='Contrato')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'db_table': 'gc_payment',
                'ordering': ['id'],
            },
        ),
    ]
