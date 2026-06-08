from rest_framework import serializers
from utils import format_date
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """Serializa os dados de notifications para a API."""
    notification_date_formatted = serializers.SerializerMethodField()

    def get_notification_date_formatted(self, obj):
        return format_date(obj.notification_date)

    class Meta:
        """Configuracao principal do serializer de notifications."""
        model = Notification
        fields = '__all__'
