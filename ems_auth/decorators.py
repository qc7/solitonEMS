from django.http import HttpResponseRedirect
from django.urls import reverse


def ems_login_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if user.is_authenticated:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('login'))

    return wrapper
