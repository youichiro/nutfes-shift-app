from rest_framework import viewsets
from apps.manual.models import Manual
from .serializer import ManualSerializer


class ManualViewSet(viewsets.ModelViewSet):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer
