from django.urls import path
from events.views import email

app_name='events'

urlpatterns=[
     path('me', email)
]