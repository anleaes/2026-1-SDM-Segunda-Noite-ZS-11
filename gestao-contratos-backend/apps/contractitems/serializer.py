from rest_framework import serializers
from .models import ContractItem

class ContractItemSerializer(serializers.ModelSerializer):
    """Serializa os dados de contractitems para a API."""
    class Meta:
        """Configuracao principal do serializer de contractitems."""
        model = ContractItem
        fields = '__all__'
