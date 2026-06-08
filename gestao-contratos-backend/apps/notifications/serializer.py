from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """Serializa os dados de notifications para a API."""
    class Meta:
        model = Notification
        fields = '__all__'
