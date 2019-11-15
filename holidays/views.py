from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from role.models import Notification

# Create your views here.
@login_required
def holidays_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'ems_auth/login.html', {"message": None})

    # Get the notifications
    user = request.user.solitonuser

    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()

    context = {
        "holidays_page": "active",
        "number_of_notifications": number_of_notifications,
    }

    return render(request, 'holidays/holidays_page.html',context)
