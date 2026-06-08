from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    """Serializa os dados de clients para a API."""
    class Meta:
        model = Client
        fields = '__all__'
