from rest_framework import serializers
from .models import ContractItem

class ContractItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractItem
        fields = '__all__'
