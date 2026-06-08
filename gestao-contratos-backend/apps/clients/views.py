from rest_framework import viewsets
from .models import Client
from .serializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de clients."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
