from rest_framework import viewsets
from .models import Service
from .serializer import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de services."""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
