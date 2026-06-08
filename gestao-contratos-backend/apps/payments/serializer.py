from rest_framework import serializers
from utils import format_currency, format_date
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    """Serializa os dados de payments para a API."""
    due_date_formatted = serializers.SerializerMethodField()
    payment_date_formatted = serializers.SerializerMethodField()
    value_formatted = serializers.SerializerMethodField()

    def get_due_date_formatted(self, obj):
        return format_date(obj.due_date)

    def get_payment_date_formatted(self, obj):
        return format_date(obj.payment_date)

    def get_value_formatted(self, obj):
        return format_currency(obj.value)

    class Meta:
        """Configuracao principal do serializer de payments."""
        model = Payment
        fields = '__all__'
