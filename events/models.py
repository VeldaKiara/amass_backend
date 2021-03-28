from django.db import models
import uuid

# Create your models here.

class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, blank=False)
    location = models.CharField(max_length=300, blank=False)
    description = models.TextField(max_length=450, blank=False)
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    
    # payment = models.ForeignKey(Payment)
    
    class Meta:
        pass
    
