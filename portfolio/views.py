from django.shortcuts import render
from contact_us.models import ContactUs
# Create your views here.
def portfolio(request):
    contact_us = ContactUs.objects.all()
    context = {
        'contact_us' : contact_us,
    }
    return render(request, 'portfolio/portfolio.html', context)

def project(request):
    contact_us = ContactUs.objects.all()
    context = {
        'contact_us' : contact_us,
    }
    return render(request, 'portfolio/project.html', context)