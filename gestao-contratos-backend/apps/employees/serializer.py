from rest_framework import serializers
from utils import format_currency, mask_phone, only_digits
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    phone_masked = serializers.SerializerMethodField()
    salary_formatted = serializers.SerializerMethodField()

    def get_phone_masked(self, obj):
        return mask_phone(obj.phone)

    def get_salary_formatted(self, obj):
        return format_currency(obj.salary)

    def validate_phone(self, value):
        return only_digits(value) or value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['phone'] = mask_phone(data.get('phone'))
        return data

    class Meta:
        model = Employee
        fields = '__all__'
