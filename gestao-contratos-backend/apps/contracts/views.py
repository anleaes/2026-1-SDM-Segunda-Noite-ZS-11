from rest_framework import viewsets
from .models import Contract
from .serializer import ContractSerializer

class ContractViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de contracts."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
