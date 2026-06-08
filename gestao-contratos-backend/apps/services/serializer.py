from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    """Serializa os dados de services para a API."""
    class Meta:
        """Configuracao principal do serializer de services."""
        model = Service
        fields = '__all__'
