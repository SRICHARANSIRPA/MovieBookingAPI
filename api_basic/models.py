# from django.db import models
# from django.contrib.auth.models import (AbstractBaseUser, AbstractUser)
# # Create your models here.
# from django.contrib.auth.models import (AbstractBaseUser, AbstractUser)
# from datetime import date, datetime
#
#
# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     date = models.DateTimeField(auto_now_add=True)
#     models
#
#     def __str__(self):
#         return self.title
#
#
# class BaseModel(models.Model):
#     CreatedTime = models.DateTimeField()
#     CreatedBy = models.IntegerField()
#     UpdatedBy = models.DateTimeField(null=True)
#     UpdatedTime = models.DateTimeField(null=True)
#
#     def __init__(self, CreatedBy, UpdatedBy):
#         self.CreatedTime = datetime.now()
#         self.CreatedBy = CreatedBy
#         self.UpdatedBy = UpdatedBy
#
#     class Meta:
#         abstract = True
#
#
# class User(BaseModel):
#     Name = models.CharField(max_length=100)
#     IsActive = models.BooleanField()
#
#     def __init__(self, Name, CreatedBy, UpdatedBy):
#         super().__init__(CreatedBy, UpdatedBy)
#         self.isActive = True
#         self.Name = Name
#
#
# class Role(BaseModel):
#     Name = models.CharField(max_length=20)
#     CanBookTicket = models.BooleanField(default=True)
#     CanCancelTicket = models.BooleanField(default=False)
#     CanAddCinema = models.BooleanField(default=False)
#     CanUpdateTicket = models.BooleanField(default=False)
#     CanAddTicket = models.BooleanField(default=False)
#
#
# class UserRole(BaseModel):
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     Role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     IsCurrent = models.BooleanField(default=False)
#
