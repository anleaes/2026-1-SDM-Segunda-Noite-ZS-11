from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializa os dados de employees para a API."""
    class Meta:
        model = Employee
        fields = '__all__'
