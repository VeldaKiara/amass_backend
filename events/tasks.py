from django.core.mail import send_mail
from django.conf import settings
from celery.decorators import task
from celery.utils.log import get_task_logger
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from events.models import Events
logger = get_task_logger(__name__)

@task(name="send_email_background")
def send_mail_background(subject, message, email_from, recipient_list):
    w=Events.objects.first()
    html_message = render_to_string('mail_template.html', {'context': 'values', 
                                                           'eve' : w,
                                                           'dt':w.event_time.strftime("%Y%m%dT%H%M00z")
                                                           })
    plain_message = strip_tags(html_message)

    mail.send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    logger.info("Sent feedback email")
    
    
    


