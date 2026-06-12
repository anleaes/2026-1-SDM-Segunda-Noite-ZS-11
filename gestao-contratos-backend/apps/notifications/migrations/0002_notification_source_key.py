from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gc_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='source_key',
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=150,
                null=True,
                unique=True,
            ),
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={
                'ordering': ['-id'],
                'verbose_name': 'Notificacao',
                'verbose_name_plural': 'Notificacoes',
            },
        ),
    ]
