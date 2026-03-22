from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from core.models import BaseModel


class UserSoftDeleteManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class User(AbstractUser,BaseModel):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank = True)
    address = models.CharField(max_length=100, blank=True)
    stripe_customer_id = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    preferences = models.JSONField(default=dict, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    objects = UserSoftDeleteManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email