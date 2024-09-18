from django.shortcuts import render
from .models import welcome_page


# Create your views here.

def home(request):
    welcome_items = welcome_page.objects.all()
    return render(request, 'home.html', {'welcome_items': welcome_items})


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')