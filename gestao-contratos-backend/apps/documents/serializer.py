from rest_framework import serializers
from utils import format_date
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    """Serializa os dados de documents para a API."""
    upload_date_formatted = serializers.SerializerMethodField()

    def get_upload_date_formatted(self, obj):
        return format_date(obj.upload_date)

    class Meta:
        """Configuracao principal do serializer de documents."""
        model = Document
        fields = '__all__'
