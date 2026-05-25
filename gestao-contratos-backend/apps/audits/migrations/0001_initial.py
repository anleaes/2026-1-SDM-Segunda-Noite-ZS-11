import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_contracts', '0001_initial'),
        ('gc_useraccounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100, verbose_name='Ação')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('action_date', models.DateField(verbose_name='Data da ação')),
                ('ip_address', models.CharField(max_length=50, verbose_name='Endereço IP')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audits', to='gc_contracts.contract', verbose_name='Contrato')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audits', to='gc_useraccounts.useraccount', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Auditoria',
                'verbose_name_plural': 'Auditorias',
                'db_table': 'gc_audit',
                'ordering': ['id'],
            },
        ),
    ]
