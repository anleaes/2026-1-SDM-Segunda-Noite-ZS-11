from rest_framework import serializers
from utils import format_currency, format_date
from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    """Serializa os dados de contracts para a API."""
    start_date = serializers.DateField(input_formats=['%Y-%m-%d', '%d/%m/%Y'])
    end_date = serializers.DateField(input_formats=['%Y-%m-%d', '%d/%m/%Y'])
    start_date_formatted = serializers.SerializerMethodField()
    end_date_formatted = serializers.SerializerMethodField()
    total_value_formatted = serializers.SerializerMethodField()

    def get_start_date_formatted(self, obj):
        return format_date(obj.start_date)

    def get_end_date_formatted(self, obj):
        return format_date(obj.end_date)

    def get_total_value_formatted(self, obj):
        return format_currency(obj.total_value)

    class Meta:
        """Configuracao principal do serializer de contracts."""
        model = Contract
        fields = '__all__'
