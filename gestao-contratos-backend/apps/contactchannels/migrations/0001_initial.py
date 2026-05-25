from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição')),
                ('channel_type', models.CharField(choices=[('EMAIL', 'Email'), ('TELEFONE', 'Telefone'), ('WHATSAPP', 'WhatsApp'), ('OUTRO', 'Outro')], max_length=20, verbose_name='Tipo de canal')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Canal de contato',
                'verbose_name_plural': 'Canais de contato',
                'db_table': 'gc_contract_channel',
                'ordering': ['id'],
            },
        ),
    ]
