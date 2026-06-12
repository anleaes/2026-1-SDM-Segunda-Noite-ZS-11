from rest_framework import serializers
from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    """Serializa os dados de useraccounts para a API."""
    class Meta:
        """Configuracao principal do serializer de useraccounts."""
        model = UserAccount
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }
