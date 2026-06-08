from rest_framework import viewsets
from .models import Payment
from .serializer import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de payments."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
