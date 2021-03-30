from django.db import models
import uuid
from payment.models import Payment
# Create your models here.
class Tickets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey('events.Events', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    payment = models.ForeignKey('payment.Payment', on_delete=models.CASCADE, null=True, blank=True)
    