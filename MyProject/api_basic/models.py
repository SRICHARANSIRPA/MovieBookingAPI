import uuid
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from datetime import datetime

# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4,primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    updated_time = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

