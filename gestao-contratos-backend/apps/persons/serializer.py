from rest_framework import serializers
from utils import mask_phone, only_digits
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """Serializa os dados de persons para a API."""
    phone_masked = serializers.SerializerMethodField()

    def get_phone_masked(self, obj):
        return mask_phone(obj.phone)

    def validate_phone(self, value):
        return only_digits(value) or value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['phone'] = mask_phone(data.get('phone'))
        return data

    class Meta:
        """Configuracao principal do serializer de persons."""
        model = Person
        fields = '__all__'
