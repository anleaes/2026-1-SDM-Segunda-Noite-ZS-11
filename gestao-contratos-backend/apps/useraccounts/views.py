from rest_framework import viewsets
from .models import UserAccount
from .serializer import UserAccountSerializer

class UserAccountViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de useraccounts."""
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
