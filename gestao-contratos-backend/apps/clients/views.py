from rest_framework import viewsets
from .models import Client
from .serializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de clients."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
