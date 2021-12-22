from django.db import models


class StatusValues(models.TextChoices):
    BOOKED = 'BOOKED'
    CANCELLED = 'CANCELLED'
