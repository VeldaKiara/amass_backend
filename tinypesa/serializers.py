from rest_framework import serializers
from events.models import Events
class TinypesaSerializer(serializers.Serializer):
    events = serializers.PrimaryKeyRelatedField(queryset = Events.objects.all())
    phone_number= serializers.CharField(required=True)