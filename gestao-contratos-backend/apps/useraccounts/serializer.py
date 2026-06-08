from rest_framework import serializers
from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    """Serializa os dados de useraccounts para a API."""
    class Meta:
        model = UserAccount
        fields = '__all__'
