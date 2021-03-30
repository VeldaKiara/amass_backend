from rest_framework import serializers
from events.models import Events

class EventsSerializer(serializers.ModelSerializer):

   class Meta:
        model = Events
        fields = ('id', 'name', 'location', 'description', 'user', 'payment')

