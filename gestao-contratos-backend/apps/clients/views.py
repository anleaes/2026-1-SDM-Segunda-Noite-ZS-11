from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from .models import Client
from .serializer import ClientSerializer

class ClientViewSet(AuditedModelViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de clients."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
