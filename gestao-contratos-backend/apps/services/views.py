from rest_framework import viewsets
from .models import Service
from .serializer import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de services."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
