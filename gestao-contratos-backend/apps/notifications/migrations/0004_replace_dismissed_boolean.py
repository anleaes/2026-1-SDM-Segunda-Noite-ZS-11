from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gc_notifications', '0003_notification_is_dismissed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_dismissed',
        ),
        migrations.AddField(
            model_name='notification',
            name='is_dismissed',
            field=models.PositiveSmallIntegerField(default=0, editable=False),
        ),
    ]
