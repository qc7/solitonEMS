from django.shortcuts import render, redirect


# Create your views here.
def about_us(request):
    return render(request, "organisation_description.html")
