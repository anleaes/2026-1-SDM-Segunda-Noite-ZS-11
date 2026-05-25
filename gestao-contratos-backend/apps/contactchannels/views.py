from rest_framework import viewsets
from .models import ContactChannel
from .serializer import ContactChannelSerializer

class ContactChannelViewSet(viewsets.ModelViewSet):
    queryset = ContactChannel.objects.all()
    serializer_class = ContactChannelSerializer
