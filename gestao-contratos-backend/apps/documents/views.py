from rest_framework import viewsets
from .models import Document
from .serializer import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de documents."""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
