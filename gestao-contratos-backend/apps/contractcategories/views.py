from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from useraccounts.access import RoleScopedViewSetMixin
from .models import ContractCategory
from .serializer import ContractCategorySerializer

class ContractCategoryViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de contractcategories."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = ContractCategory.objects.all()
    serializer_class = ContractCategorySerializer
    employee_allowed_actions = ('list', 'retrieve')
    employee_filter = 'contract__employee_id'
