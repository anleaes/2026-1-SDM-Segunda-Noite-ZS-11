from rest_framework import serializers
from utils import mask_cpf_cnpj, mask_phone, only_digits
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    cpf_cnpj_masked = serializers.SerializerMethodField()
    phone_masked = serializers.SerializerMethodField()

    def get_cpf_cnpj_masked(self, obj):
        return mask_cpf_cnpj(obj.cpf_cnpj)

    def get_phone_masked(self, obj):
        return mask_phone(obj.phone)

    def validate_cpf_cnpj(self, value):
        return only_digits(value) or value

    def validate_phone(self, value):
        return only_digits(value) or value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cpf_cnpj'] = mask_cpf_cnpj(data.get('cpf_cnpj'))
        data['phone'] = mask_phone(data.get('phone'))
        return data

    class Meta:
        model = Client
        fields = '__all__'
