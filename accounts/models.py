from django.db import models
from django.contrib.auth.models import AbstractUser
from events.models import Events
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email =  models.EmailField('email address', max_length=254, blank=False, unique = True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    
    
    class Meta:
        pass
    def __str__(self):
        return self.username
