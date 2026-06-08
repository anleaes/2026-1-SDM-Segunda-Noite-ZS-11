from rest_framework import serializers
from .models import ContractItem

class ContractItemSerializer(serializers.ModelSerializer):
    """Serializa os dados de contractitems para a API."""
    class Meta:
        model = ContractItem
        fields = '__all__'
