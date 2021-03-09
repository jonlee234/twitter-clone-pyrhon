from django.shortcuts import render, redirect, reverse
from tweet.forms import TweetForm
from tweet.models import Tweet
from django.contrib.auth import get_user_model

MyUser = get_user_model()
# Create your views here.


def post_tweet(request):
    context = {}
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newitem = Tweet.objects.create(
                tweet=data['tweet'],
                author=MyUser.objects.filter(id=request.user.id).first(),
            )
            return redirect(reverse("home"))
    form = TweetForm
    context.update({'form': form})
    return render(request, "generic_form.html", {'form': form})


def discover_view(request):
    tweets = Tweet.objects.all()
    return render(request, 'discover.html', {"tweets": tweets})
