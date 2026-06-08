from rest_framework import serializers
from utils import format_date
from .models import Audit

class AuditSerializer(serializers.ModelSerializer):
    action_date_formatted = serializers.SerializerMethodField()

    def get_action_date_formatted(self, obj):
        return format_date(obj.action_date)

    class Meta:
        model = Audit
        fields = '__all__'
