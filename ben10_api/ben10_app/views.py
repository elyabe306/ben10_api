from rest_framework import viewsets
from .models import Alien
from .serializers import AlienSerializer

class AlienViewSet(viewsets.ModelViewSet):
    queryset = Alien.objects.all()
    serializer_class = AlienSerializer