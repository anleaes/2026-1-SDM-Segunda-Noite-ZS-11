from rest_framework import viewsets
from .models import ContractCategory
from .serializer import ContractCategorySerializer

class ContractCategoryViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de contractcategories."""
    queryset = ContractCategory.objects.all()
    serializer_class = ContractCategorySerializer
