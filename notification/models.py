from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.utils import timezone

# Create your models here.


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    post_time = models.DateField(default=timezone.now)
    mentions = models.ManyToManyField(TwitterUser, symmetrical=False)


def __str__(self):
    return f"{self.tweet} - {', '.join([str(p)for p in self.mentions.all()])}"
