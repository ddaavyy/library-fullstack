from rest_framework import viewsets
from .models import LivrosModel
from .serializers import LivrosSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = LivrosModel.objects.all()
    serializer_class = LivrosSerializer
