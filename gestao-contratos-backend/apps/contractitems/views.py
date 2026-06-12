from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from .models import ContractItem
from .serializer import ContractItemSerializer

class ContractItemViewSet(AuditedModelViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de contractitems."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = ContractItem.objects.all()
    serializer_class = ContractItemSerializer
