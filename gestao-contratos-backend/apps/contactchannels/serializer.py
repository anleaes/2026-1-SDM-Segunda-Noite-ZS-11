from rest_framework import serializers
from .models import ContactChannel

class ContactChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactChannel
        fields = '__all__'
