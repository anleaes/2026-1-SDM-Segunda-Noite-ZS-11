from rest_framework import serializers
from .models import ContractCategory

class ContractCategorySerializer(serializers.ModelSerializer):
    """Serializa os dados de contractcategories para a API."""
    class Meta:
        """Configuracao principal do serializer de contractcategories."""
        model = ContractCategory
        fields = '__all__'
