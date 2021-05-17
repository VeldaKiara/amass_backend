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
from events.tasks import send_mail_background
from django.conf import settings
import ast

class TinypesaViewSets(viewsets.ViewSet):
     @action(detail=False, methods=['post'])
     def start (self, request):
         
           
                 
        #  subject = 'Thank you for registering to our site'
        #  message = ' it  means a world to us '
        #  email_from = settings.EMAIL_HOST_USER
        #  recipient_list = ['shecodeafricanairobi@gmail.com',]
         
        #  send_mail_background.delay( subject, message, email_from, recipient_list,event_id )
                        
         s = TinypesaSerializer(data = request.data)
        
         if not s.is_valid():
            
             return Response(s.errors)
        
         event_id=request.data.get('events')
         event=Events.objects.get(pk=event_id)
         t=request.data.get('ticket_number')
         print(t)
         total_amnt= float(event.cost) * float(t)
        
         
         url = 'https://tinypesa.com/api/v1/express/initialize'
         body = {
             'msisdn': s.data.get('phone_number'),
             'amount': str(total_amnt)
             }
         headers = {'Accept': 'application/json',
                    'Apikey': '5fLaVcPJh7n'
                    
                    }

         r = requests.post(url,data=body, headers=headers)
         data = json.loads(r.text)
         e= Events.objects.get(pk=s.data.get('events'))
        #  auser = request.user.id
        #  print(auser)
         Payment.objects.create(event=e , ref_number = data['request_id'], user_id=request.user)
           
            

         return Response({'status': 'transaction started'})
     
     @action(detail=False, methods=['post'])
     def webhook(self, request):
         
         v = Payment.objects.filter(ref_number = request.data['Body']['stkCallback']['TinyPesaID']).first()
         u = CustomUser.objects.get(id = v.user_id.id)
         
        
         if v:
             if request.data['Body']['stkCallback']['ResultCode'] == 0 :
                 v.status = 1
                 v.save()
                 
                 current_event = Events.objects.get(pk=v.event.id)
                 n = int(float(request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value'])/ current_event.cost)
                 for i in range(0,n):
                    Tickets.objects.create(event=v.event, payment=v, user=CustomUser.objects.first()) 
                    subject = 'Thank you for registering to our site'
                    message = ' it  means the world to us '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [u.email]
         
                    send_mail_background.delay( subject, message, email_from, recipient_list, v.event_id )
                    
                    
                
         return Response({'velda':request.data['Body']})
        #  return Response({'velda':"makiria"})
     
         
         
