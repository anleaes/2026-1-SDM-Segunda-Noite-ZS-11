from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from useraccounts.access import RoleScopedViewSetMixin
from .models import Client
from .serializer import ClientSerializer

class ClientViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de clients."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    employee_allowed_actions = ('list', 'retrieve')
    employee_filter = 'contract__employee_id'
