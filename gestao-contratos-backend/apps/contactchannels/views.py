from rest_framework import viewsets
from .models import ContactChannel
from .serializer import ContactChannelSerializer

class ContactChannelViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de contactchannels."""
    queryset = ContactChannel.objects.all()
    serializer_class = ContactChannelSerializer
