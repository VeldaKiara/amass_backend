from django.shortcuts import render
from events.tasks import send_mail_background
from django.conf import settings
from django.http import HttpResponse



def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['shecodeafricanairobi@gmail.com',]
    send_mail_background.delay( subject, message, email_from, recipient_list )
    return HttpResponse('redirect to a new page')