from django.db import models
import uuid

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    type = models.TextField(default= "default_type")
    quality = models.CharField(max_length=7, default= "default_quality")
    description = models.TextField()
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)