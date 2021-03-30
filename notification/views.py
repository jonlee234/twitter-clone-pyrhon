from django.shortcuts import render
from twitteruser.models import TwitterUser
from notification.models import Notification


# Create your views here.

def notification_view(request):
    u = TwitterUser.objects.get(id=request.user.id)
    notifications = Notification.objects.filter(mentions=request.user.id).all()
    context = {"notifications": notifications}
    notes = Notification.objects.filter(mentions=u).all()
    responce = render(request, "notifications.html", context)
    for note in notes:
        note.mentions.remove(u)
        note.save()
    return responce
