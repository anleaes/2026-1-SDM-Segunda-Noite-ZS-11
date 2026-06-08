from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    """Serializa os dados de documents para a API."""
    class Meta:
        model = Document
        fields = '__all__'
