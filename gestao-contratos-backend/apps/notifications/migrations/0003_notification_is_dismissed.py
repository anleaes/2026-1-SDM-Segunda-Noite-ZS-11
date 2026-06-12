from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gc_notifications', '0002_notification_source_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_dismissed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
