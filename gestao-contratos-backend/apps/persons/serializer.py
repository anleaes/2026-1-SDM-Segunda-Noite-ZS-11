from rest_framework import serializers
from utils import mask_phone
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    phone_masked = serializers.SerializerMethodField()

    def get_phone_masked(self, obj):
        return mask_phone(obj.phone)

    class Meta:
        model = Person
        fields = '__all__'
