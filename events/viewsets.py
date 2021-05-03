from rest_framework import viewsets
from .models import Events
from .serializers import EventsSerializer
from rest_framework.response import Response
class EventsViewSets(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    def create(self, request):
        s=EventsSerializer(data=request.data)
        if s.is_valid():
            s.save(user=request.user)
            return Response(s.data)
        else: 
            return Response(s.errors)

    