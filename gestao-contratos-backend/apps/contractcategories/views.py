from rest_framework import viewsets
from .models import ContractCategory
from .serializer import ContractCategorySerializer

class ContractCategoryViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de contractcategories."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = ContractCategory.objects.all()
    serializer_class = ContractCategorySerializer
