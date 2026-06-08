from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """Serializa os dados de persons para a API."""
    class Meta:
        """Configuracao principal do serializer de persons."""
        model = Person
        fields = '__all__'
