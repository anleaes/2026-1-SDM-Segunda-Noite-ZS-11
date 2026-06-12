from rest_framework import viewsets
from audits.mixins import AuditedModelViewSetMixin
from useraccounts.access import RoleScopedViewSetMixin
from .models import Employee
from .serializer import EmployeeSerializer

class EmployeeViewSet(AuditedModelViewSetMixin, RoleScopedViewSetMixin, viewsets.ModelViewSet):
    """Endpoint REST para operacoes de employees."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    employee_allowed_actions = ('list', 'retrieve')
    employee_filter = 'id'
