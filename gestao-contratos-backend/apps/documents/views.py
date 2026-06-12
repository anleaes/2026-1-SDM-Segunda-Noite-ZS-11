from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from useraccounts.access import RoleScopedViewSetMixin
from .models import Document
from .serializer import DocumentSerializer

class DocumentViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de documents."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    employee_allowed_actions = ('list', 'retrieve')
    employee_filter = 'contract__employee_id'
