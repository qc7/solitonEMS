from django.http import HttpResponseRedirect
from django.urls import reverse

from ems_auth.models import SolitonUser
from organisation_details.selectors import get_organisationdetail


def organisationdetail_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        try:
            organisationdetail = get_organisationdetail(user)

        except SolitonUser.DoesNotExist:
            organisationdetail = None

        if organisationdetail:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('no_organisation_detail_page'))

    return wrapper
