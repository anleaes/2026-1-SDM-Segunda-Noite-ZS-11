from rest_framework import serializers
from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    """Serializa os dados de contracts para a API."""
    class Meta:
        model = Contract
        fields = '__all__'
