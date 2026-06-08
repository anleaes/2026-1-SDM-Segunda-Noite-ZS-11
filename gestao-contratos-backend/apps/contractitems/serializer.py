from rest_framework import serializers
from utils import format_currency
from .models import ContractItem

class ContractItemSerializer(serializers.ModelSerializer):
    unitary_price_formatted = serializers.SerializerMethodField()
    total_price_formatted = serializers.SerializerMethodField()

    def get_unitary_price_formatted(self, obj):
        return format_currency(obj.unitary_price)

    def get_total_price_formatted(self, obj):
        return format_currency(obj.total_price)

    class Meta:
        model = ContractItem
        fields = '__all__'
