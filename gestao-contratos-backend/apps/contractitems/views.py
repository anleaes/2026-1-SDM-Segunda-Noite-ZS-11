from rest_framework import viewsets
from .models import ContractItem
from .serializer import ContractItemSerializer

class ContractItemViewSet(viewsets.ModelViewSet):
    queryset = ContractItem.objects.all()
    serializer_class = ContractItemSerializer
