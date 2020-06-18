from django.shortcuts import redirect, render

from .models import Notification
from .selectors import read_all_notifications,  get_recent_notification


# Create your views here.

def notifications_page(request):
    user = request.user
    read_all_notifications(user)
    context = {
        "notifications": get_recent_notification(user)
    }

    return render(request, "notifications/notifications.html", context)
