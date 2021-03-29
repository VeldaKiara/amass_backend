from rest_framework import serializers
from tickets.models import Tickets

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('id', 'event','user')