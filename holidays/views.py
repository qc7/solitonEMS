from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def holidays_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'ems_auth/login.html', {"message": None})

    # Get the notifications
    user = request.user.solitonuser

    context = {
        "holidays_page": "active",
    }

    return render(request, 'holidays/holidays_page.html', context)
