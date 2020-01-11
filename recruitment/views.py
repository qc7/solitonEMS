from django.shortcuts import render


# Create your views here.
from organisation_details.selectors import get_all_positions


def manage_job_advertisement_page(request):

    all_positions = get_all_positions()
    context = {
        "recruitment_page": "active",
        "positions": all_positions
    }
    return render(request, 'recruitment/manage_job_advertisement.html', context)
