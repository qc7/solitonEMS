from django.shortcuts import redirect, render
from .models import Notification
from .selectors import get_notification

# Create your views here.

def notifications_page(request, id):
    user = request.user
    notification = get_notification(id)

    notification_type = notification.title

    if notification_type == "Leave":
        Notification.objects.filter(title="Leave", user=user).update(status = "Read")

        return redirect("leave_dashboard_page")
    elif notification_type == "Overtime":
        Notification.objects.filter(title="Overtime", user=user).update(status = "Read")

        return redirect("leave_dashboard_page")