from django.http import HttpResponseRedirect
from django.urls import reverse

from organisation_details.selectors import get_organisationdetail
from organisation_details.views import no_organisation_detail_page


def organisationdetail_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        organisationdetail = get_organisationdetail(user)
        if organisationdetail:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('no_organisation_detail_page'))

    return wrapper
