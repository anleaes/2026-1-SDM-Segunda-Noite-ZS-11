from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from notifications.services import create_payment_overdue_notification
from useraccounts.access import RoleScopedViewSetMixin
from .models import Payment
from .serializer import PaymentSerializer

class PaymentViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de payments."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    employee_allowed_actions = ('list', 'retrieve')
    employee_filter = 'contract__employee_id'

    def perform_create(self, serializer):
        super().perform_create(serializer)
        create_payment_overdue_notification(serializer.instance)

    def perform_update(self, serializer):
        super().perform_update(serializer)
        create_payment_overdue_notification(serializer.instance)
