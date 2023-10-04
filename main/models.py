from django.db import models
import uuid
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    type = models.TextField(default= "default_type")
    quality = models.CharField(max_length=7, default= "default_quality")
    description = models.TextField()
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    