from django.db import migrations, models


def rename_operator_profile(apps, schema_editor):
    UserAccount = apps.get_model('gc_useraccounts', 'UserAccount')
    UserAccount.objects.filter(profile='OPERADOR').update(profile='FUNCIONARIO')


class Migration(migrations.Migration):

    dependencies = [
        ('gc_useraccounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(rename_operator_profile, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='useraccount',
            name='profile',
            field=models.CharField(
                choices=[
                    ('ADMIN', 'Administrador'),
                    ('GERENTE', 'Gerente'),
                    ('FUNCIONARIO', 'Funcionario'),
                ],
                max_length=20,
                verbose_name='Perfil',
            ),
        ),
    ]
