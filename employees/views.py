from django.shortcuts import render

# Create your views here.

# dashboard
def index(request):
    return render(request,'employees/dashboard.html') 