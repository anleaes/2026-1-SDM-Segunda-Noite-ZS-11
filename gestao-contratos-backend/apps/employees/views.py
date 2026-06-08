from rest_framework import viewsets
from .models import Employee
from .serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de employees."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
