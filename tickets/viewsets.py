from rest_framework import viewsets
from .models import Tickets
from .serializers import TicketsSerializer

class TicketsViewSets(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer