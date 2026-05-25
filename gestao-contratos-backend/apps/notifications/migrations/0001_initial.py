import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('message', models.TextField(max_length=500, verbose_name='Mensagem')),
                ('notification_date', models.DateField(verbose_name='Data da notificação')),
                ('notification_type', models.CharField(choices=[('VENCIMENTO', 'Vencimento'), ('PAGAMENTO', 'Pagamento'), ('DOCUMENTO', 'Documento'), ('GERAL', 'Geral')], default='GERAL', max_length=20, verbose_name='Tipo de notificação')),
                ('is_read', models.BooleanField(default=False, verbose_name='Lida')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='gc_contracts.contract', verbose_name='Contrato')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
                'db_table': 'gc_notification',
                'ordering': ['id'],
            },
        ),
    ]
