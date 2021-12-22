from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from MyProject.api_basic.models import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=12)
    age = models.IntegerField(null=True)
    activation_date = models.DateTimeField(default=timezone.now)


class Role(BaseModel):
    name = models.CharField(max_length=20)
    can_book_ticket = models.BooleanField(default=True)
    can_cancel_ticket = models.BooleanField(default=False)
    can_add_cinema = models.BooleanField(default=False)
    can_update_ticket = models.BooleanField(default=False)
    can_add_ticket = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserRole(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username+ ' - ' + self.role.name
