from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def settings_page(request):

    return render(request, 'settings/settings_page.html')