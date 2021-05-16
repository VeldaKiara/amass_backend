from rest_framework import serializers
from events.models import Events
from accounts.serializers import CustomUserSerializer

class EventsSerializer(serializers.ModelSerializer):

   detailed_user = CustomUserSerializer(source='user', required=False)
   class Meta:
        model = Events
        fields = ('id', 'name', 'location', 'description', 'event_time', 'user', 'is_paid','cost','detailed_user')
        read_only_fields = ('user','detailed_user')
