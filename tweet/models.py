from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.


class Tweet(models.Model):
    tweet = models.TextField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)


def __unicode__(self):
    return self.tweet
