from django.shortcuts import render, redirect, reverse
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.contrib.auth import get_user_model
import re

MyUser = get_user_model()
# Create your views here.


def find_mention_names(name, tweet):
    if not TwitterUser.objects.get(username=name):
        return
    u = TwitterUser.objects.get(username=name)
    n = Notification.objects.create(tweet=tweet)
    n.mentions.add(u)
    if not n.mentions:
        n.delete()
    n.save()


def post_tweet(request):
    context = {}
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newitem = Tweet.objects.create(
                tweet=data['tweet'],
                author=request.user,
            )
            x = re.findall(r'@([A-Za-z0-9_]+)', newitem.tweet)
            for name in x:
                find_mention_names(name, newitem)
            return redirect(reverse("home"))
    form = TweetForm
    context.update({'form': form})
    return render(request, "generic_form.html", {'form': form})


def discover_view(request):
    tweets = Tweet.objects.all()
    return render(request, 'discover.html', {"tweets": tweets})


def tweet_detail(request, post_id):
    tweet = Tweet.objects.get(id=post_id)
    return render(request, 'tweet_detail.html', {"tweet": tweet})
