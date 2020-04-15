from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255, default='', blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=255, default='', blank=True, verbose_name='Last Name')

