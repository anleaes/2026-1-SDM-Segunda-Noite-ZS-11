from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição')),
                ('priority_level', models.IntegerField(default=1, verbose_name='Nível de prioridade')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Categoria de contrato',
                'verbose_name_plural': 'Categorias de contrato',
                'db_table': 'gc_contract_category',
                'ordering': ['id'],
            },
        ),
    ]
