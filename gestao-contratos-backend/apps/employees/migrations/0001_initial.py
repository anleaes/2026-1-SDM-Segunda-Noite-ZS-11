import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gc_persons.person')),
                ('registration', models.CharField(max_length=30, unique=True, verbose_name='Matrícula')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
                ('department', models.CharField(max_length=100, verbose_name='Departamento')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Salário')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'db_table': 'gc_employee',
                'ordering': ['id'],
            },
            bases=('gc_persons.person',),
        ),
    ]
