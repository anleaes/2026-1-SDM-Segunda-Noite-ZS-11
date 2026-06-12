from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from useraccounts.access import RoleScopedViewSetMixin
from .models import Person
from .serializer import PersonSerializer

class PersonViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de persons."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
