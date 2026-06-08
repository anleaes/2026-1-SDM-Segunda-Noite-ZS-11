from rest_framework import serializers
from utils import mask_phone
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """Serializa os dados de persons para a API."""
    phone_masked = serializers.SerializerMethodField()

    def get_phone_masked(self, obj):
        return mask_phone(obj.phone)

    class Meta:
        """Configuracao principal do serializer de persons."""
        model = Person
        fields = '__all__'
