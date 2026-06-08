from rest_framework import serializers
from utils import mask_cpf_cnpj, mask_phone
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    cpf_cnpj_masked = serializers.SerializerMethodField()
    phone_masked = serializers.SerializerMethodField()

    def get_cpf_cnpj_masked(self, obj):
        return mask_cpf_cnpj(obj.cpf_cnpj)

    def get_phone_masked(self, obj):
        return mask_phone(obj.phone)

    class Meta:
        model = Client
        fields = '__all__'
