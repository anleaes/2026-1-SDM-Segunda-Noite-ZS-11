from rest_framework import serializers
from utils import format_currency, mask_phone
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializa os dados de employees para a API."""
    phone_masked = serializers.SerializerMethodField()
    salary_formatted = serializers.SerializerMethodField()

    def get_phone_masked(self, obj):
        return mask_phone(obj.phone)

    def get_salary_formatted(self, obj):
        return format_currency(obj.salary)

    class Meta:
        """Configuracao principal do serializer de employees."""
        model = Employee
        fields = '__all__'
