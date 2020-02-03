from django.shortcuts import render


# Create your views here.

def user_training_page(request):
    context = {
        "training_page": "active"
    }

    return render(request, 'training/user_training.html', context)
