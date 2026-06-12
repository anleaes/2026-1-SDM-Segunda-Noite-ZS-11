from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from useraccounts.access import RoleScopedViewSetMixin
from .models import Service
from .serializer import ServiceSerializer

class ServiceViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de services."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    employee_allowed_actions = ('list', 'retrieve')
    employee_filter = 'contract_items__contract__employee_id'
