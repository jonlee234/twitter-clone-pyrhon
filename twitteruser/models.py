from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from tweet.models import Tweet
# Create your models here


class TwitterUser(AbstractUser):
    tweets = models.ManyToManyField(Tweet, blank=True)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True)
