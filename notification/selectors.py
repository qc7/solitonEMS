from .models import Notification

def get_user_notifications(user):
    notifications = Notification.objects.filter(user=user, status="Unread")

    return notifications

def get_notification(notification_id):
    notification = Notification.objects.get(pk=notification_id)

    return notification