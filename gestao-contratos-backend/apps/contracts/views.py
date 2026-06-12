from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from notifications.services import create_contract_expiration_notification
from .models import Contract
from .serializer import ContractSerializer

class ContractViewSet(AuditedModelViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de contracts."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        create_contract_expiration_notification(serializer.instance)

    def perform_update(self, serializer):
        super().perform_update(serializer)
        create_contract_expiration_notification(serializer.instance)
