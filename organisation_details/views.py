from django.shortcuts import render, redirect


# Create your views here.
def about_us(request):
    return render(request, "organisation_description.html")


def no_organisation_detail_page(request):
    context = {
        "organisation_detail_page": "active"
    }
    return render(request, 'no_organisation_detail.html', context)
