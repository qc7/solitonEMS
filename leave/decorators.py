from django.http import HttpResponseRedirect
from django.urls import reverse

from leave.selectors import get_leave_record
from leave.models import Leave_Records

def leave_record_required(function):
    def wrapper(request, *args, **kw):
        employee = request.user.solitonuser.employee
        try:
            Leave_Record = get_leave_record(employee)

        except Leave_Records.DoesNotExist:
            Leave_Record = None

        if Leave_Record:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('no_leave_record_page'))

    return wrapper