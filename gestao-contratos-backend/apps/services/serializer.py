from rest_framework import serializers
from utils import format_currency
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    unit_price_formatted = serializers.SerializerMethodField()

    def get_unit_price_formatted(self, obj):
        return format_currency(obj.unit_price)

    class Meta:
        model = Service
        fields = '__all__'
