import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_contractchannels', '0001_initial'),
        ('gc_persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gc_persons.person')),
                ('cpf_cnpj', models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ')),
                ('company_name', models.CharField(max_length=150, verbose_name='Razão social/Nome fantasia')),
                ('client_type', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2, verbose_name='Tipo de cliente')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('contact_channels', models.ManyToManyField(blank=True, to='gc_contractchannels.contactchannel', verbose_name='Canais de contato')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'gc_client',
                'ordering': ['id'],
            },
            bases=('gc_persons.person',),
        ),
    ]
