from rest_framework import serializers
from .models import ContactChannel

class ContactChannelSerializer(serializers.ModelSerializer):
    """Serializa os dados de contactchannels para a API."""
    class Meta:
        model = ContactChannel
        fields = '__all__'
