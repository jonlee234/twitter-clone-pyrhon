from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from django.contrib.auth import get_user_model

# Create your views here

myUser = get_user_model()


def user_page(request, user_id):
    user_obj = TwitterUser.objects.get(id=user_id)

    tweets = Tweet.objects.filter(author=user_obj)
    count = Tweet.objects.filter(author=user_obj).count()

    return render(request, "user_detail.html", {"u": user_obj, "tweets": tweets, "count": count})


def follow_view(request, user_id):
    followee = TwitterUser.objects.get(id=user_id)
    follower = request.user
    follower.following.add(followee)
    return HttpResponseRedirect(reverse('user_detail', args=[user_id]))


def unfollow_view(request, user_id):
    followee = TwitterUser.objects.get(id=user_id)
    follower = request.user
    follower.following.remove(followee)
    return HttpResponseRedirect(reverse('user_detail', args=[user_id]))
