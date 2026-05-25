from rest_framework import serializers
from .models import ContractCategory

class ContractCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractCategory
        fields = '__all__'
