from django.db import models
import uuid
# Create your models here.
class Payment(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        ref_number = models.CharField(max_length=300, blank=False)
