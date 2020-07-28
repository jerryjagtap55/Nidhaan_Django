from django.shortcuts import render
from contact_us.models import ContactUs

# Create your views here.
def index(request):
    contact_us = ContactUs.objects.all()
    context = {
        "home_page" : "active",
        'contact_us' : contact_us,
    }
    return render(request, 'pages/index.html', context)
