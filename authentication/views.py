from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.conf import settings
from authentication.forms import LoginForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    pass
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password']
                                )
            if user:
                login(request, user)

        return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data['username'], password=data['password']
            )
            TwitterUser.objects.create()

        return HttpResponseRedirect(reverse("home"))
    form = UserForm
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
