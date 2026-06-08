from rest_framework import viewsets
from .models import Audit
from .serializer import AuditSerializer

class AuditViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de audits."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
