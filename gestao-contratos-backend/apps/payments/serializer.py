from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    """Serializa os dados de payments para a API."""
    class Meta:
        model = Payment
        fields = '__all__'
