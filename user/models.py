from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone
from graphql_jwt.signals import token_issued

from workshop.models import Topic


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255, default='', blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=255, default='', blank=True, verbose_name='Last Name')

    interestedTopics = models.ManyToManyField(Topic, blank=True)


# user login function that stores last login timestamp when a user login
def handle_user_login(sender, user, request, **kwargs):
    user.last_login = timezone.now()
    user.save()


# token_issued signal is connected with the login handler function
token_issued.connect(handle_user_login)
