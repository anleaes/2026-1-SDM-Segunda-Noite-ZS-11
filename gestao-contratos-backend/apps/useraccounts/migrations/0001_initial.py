import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gc_employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Usuário')),
                ('password', models.CharField(max_length=100, verbose_name='Senha')),
                ('profile', models.CharField(choices=[('ADMIN', 'Administrador'), ('GERENTE', 'Gerente'), ('OPERADOR', 'Operador')], max_length=20, verbose_name='Perfil')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gc_employees.employee', verbose_name='Funcionário')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'gc_user_account',
                'ordering': ['id'],
            },
        ),
    ]
