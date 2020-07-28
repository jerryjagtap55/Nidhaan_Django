from django.shortcuts import render
from .models import ContactUs

# Create your views here.
def contact_us(request):

    contact_us = ContactUs.objects.all()
    
    context = {
        'contact_us' : contact_us,

    }
    return render(request, 'contact_us/contact_us.html', context)