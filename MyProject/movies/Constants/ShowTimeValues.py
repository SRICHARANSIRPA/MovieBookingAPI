from django.db import models


class ShowTimeValues(models.TextChoices):
    MorningShow = 'MorningShow'
    MatineeShow = 'MatineeShow'
    FirstShow = 'FirstShow'
    SecondShow = 'SecondShow'
