import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gc_audits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='contract',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='audits',
                to='gc_contracts.contract',
                verbose_name='Contrato',
            ),
        ),
        migrations.AlterField(
            model_name='audit',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='audits',
                to='gc_useraccounts.useraccount',
                verbose_name='Usuario',
            ),
        ),
        migrations.AlterModelOptions(
            name='audit',
            options={
                'ordering': ['-id'],
                'verbose_name': 'Auditoria',
                'verbose_name_plural': 'Auditorias',
            },
        ),
    ]
