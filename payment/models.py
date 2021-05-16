from django.db import models
import uuid
from events.models import Events
from accounts.models import CustomUser
# Create your models here.
PAYMENT_STATES=[
        (0,'Pending'),
        (1, 'Success'),
        (2,'Cancelled'),
        (3,'Failed')
]
class Payment(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user_id = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, null=True)
        ref_number = models.CharField(max_length=300, blank=False)
        event = models.ForeignKey("events.Events", on_delete=models.CASCADE, null=True)
        status = models.IntegerField(choices=PAYMENT_STATES, default=0)
