from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from audits.mixins import AuditedModelViewSetMixin
from audits.services import record_audit_event
from .models import Notification
from .serializer import NotificationSerializer
from .services import generate_system_notifications

class NotificationViewSet(AuditedModelViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de notifications."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Notification.objects.select_related('contract').filter(is_dismissed=0)
    serializer_class = NotificationSerializer

    def list(self, request, *args, **kwargs):
        generate_system_notifications()
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'], url_path='mark-read')
    def mark_read(self, request, pk=None):
        notification = self.get_object()

        if not notification.is_read:
            notification.is_read = True
            notification.save(update_fields=['is_read'])

        return Response(self.get_serializer(notification).data)

    def perform_destroy(self, instance):
        if not instance.source_key:
            super().perform_destroy(instance)
            return

        description = self.get_audit_description('Exclusao', instance)
        instance.is_dismissed = 1
        instance.save(update_fields=['is_dismissed'])
        record_audit_event(
            request=self.request,
            action=self.audit_actions['delete'],
            description=description,
            instance=instance,
        )
