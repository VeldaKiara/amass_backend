from rest_framework import viewsets
from .models import Events
from .serializers import EventsSerializer

class EventsViewSets(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    