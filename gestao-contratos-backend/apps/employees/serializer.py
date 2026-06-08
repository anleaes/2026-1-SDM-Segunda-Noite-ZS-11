from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializa os dados de employees para a API."""
    class Meta:
        """Configuracao principal do serializer de employees."""
        model = Employee
        fields = '__all__'
