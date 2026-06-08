from rest_framework import viewsets
from .models import Person
from .serializer import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """Endpoint REST para operacoes de persons."""
    # Mantem a consulta base explicita para o roteamento da API.
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
