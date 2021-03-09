from django.shortcuts import render
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your views here


def user_page(request, user_id):
    user_obj = TwitterUser.objects.get(id=user_id)

    tweets = Tweet.objects.filter(author=user_obj)
    count = Tweet.objects.filter(author=user_obj).count()

    return render(request, "user_detail.html", {"user": user_obj, "tweets": tweets, "count": count})
