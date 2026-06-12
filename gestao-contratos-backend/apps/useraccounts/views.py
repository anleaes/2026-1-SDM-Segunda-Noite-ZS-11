from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from .access import RoleScopedViewSetMixin
from .models import UserAccount
from .serializer import UserAccountSerializer

class UserAccountViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de useraccounts."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    manager_allowed_actions = ('list', 'retrieve')
    employee_allowed_actions = ('list', 'retrieve')
    employee_filter = 'employee_id'
