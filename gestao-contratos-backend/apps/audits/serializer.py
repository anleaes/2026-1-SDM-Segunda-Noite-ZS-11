from rest_framework import serializers
from .models import Audit

class AuditSerializer(serializers.ModelSerializer):
    """Serializa os dados de audits para a API."""
    class Meta:
        model = Audit
        fields = '__all__'
