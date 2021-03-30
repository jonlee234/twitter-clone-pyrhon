"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views
from tweet.views import post_tweet, discover_view, tweet_detail
from authentication.views import signup_view, login_view, logout_view
from twitteruser.views import user_page, follow_view, unfollow_view
from notification.views import notification_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path('tweets/add/', post_tweet, name='post_tweet'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('discover/', discover_view, name='discover'),
    path('users/<int:user_id>/', user_page, name="user_detail"),
    path('follow/<int:user_id>/', follow_view, name="follow_view"),
    path('unfollow/<int:user_id>/', unfollow_view, name="unfollow_view"),
    path('notifications/', notification_view, name="notification_view"),
    path('tweet/<int:post_id>/', tweet_detail, name="tweet_detail")
]
