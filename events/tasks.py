from django.core.mail import send_mail
from django.conf import settings
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name="send_email_background")
def send_mail_background(subject, message, email_from, recipient_list):
    send_mail( subject, message, email_from, recipient_list )
    logger.info("Sent feedback email")