from rest_framework import viewsets
from .models import Contract
from .serializer import ContractSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
