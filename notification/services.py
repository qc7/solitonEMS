import datetime

from .models import Notification
from ems_admin.models import User


def create_notification(title, message, receivers):
    for receiver in receivers:
        user = User.objects.get(pk=receiver.id)

        notification = Notification.objects.create(
            title=title,
            message=message,
            date_time=datetime.date.today(),
            user=user
        )


