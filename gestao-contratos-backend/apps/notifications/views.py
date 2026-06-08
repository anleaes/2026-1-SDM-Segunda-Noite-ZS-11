from rest_framework import viewsets
from .models import Notification
from .serializer import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de notifications."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
