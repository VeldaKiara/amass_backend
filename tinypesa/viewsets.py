from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TinypesaSerializer
import requests
import json
from payment.models import Payment
from tickets.models import Tickets
from accounts.models import CustomUser
from events.models import Events
class TinypesaViewSets(viewsets.ViewSet):
     @action(detail=False, methods=['post'])
     def start (self, request):
         s = TinypesaSerializer(data = request.data)
         if not s.is_valid():
             return Response(s.errors)
         url = 'https://tinypesa.com/api/v1/express/initialize'
         body = {
             'msisdn': s.data.get('phone_number'),
             'amount': 1
             }
         headers = {'Accept': 'application/json',
                    'Apikey': '5fLaVcPJh7n'
                    
                    }

         r = requests.post(url,data=body, headers=headers)
         data = json.loads(r.text)
         e= Events.objects.get(pk=s.data.get('events'))
         Payment.objects.create(event=e , ref_number = data['request_id'] )
           
            
         
         return Response({'status': 'transaction started'})
     
     @action(detail=False, methods=['post'])
     def webhook(self, request):
         v = Payment.objects.filter(ref_number=request.data['Body']['stkCallback']['TinyPesaID']).first()
         if v:
             if request.data['Body']['stkCallback']['ResultCode'] == 0 :
                 v.status = 1
                 v.save()
                 current_event = Events.objects.get(pk=v.event.id)
                 n = int(float(request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value'])/ current_event.cost)
                 for i in range(0,n):
                    Tickets.objects.create(event=v.event, payment=v, user=CustomUser.objects.first()) 
             
         
         return Response({'velda': 'engineer'})
     
     
         
        
