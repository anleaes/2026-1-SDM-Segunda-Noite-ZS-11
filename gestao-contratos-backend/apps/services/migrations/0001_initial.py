from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preço unitário')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'db_table': 'gc_service',
                'ordering': ['id'],
            },
        ),
    ]
