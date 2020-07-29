from django.shortcuts import render, get_object_or_404
from contact_us.models import ContactUs
from about.models import About, Service, Detail
from blog.models import Project, CurrentSite
from portfolio.models import Portfolio

# Create your views here.
def index(request):
    about = About.objects.all()
    service = Service.objects.all()
    detail = Detail.objects.all()
    contact_us = ContactUs.objects.all()
    project = Project.objects.all()
    currentSite = CurrentSite.objects.all()
    portfolio = Portfolio.objects.all()

    context = {
        "home_page" : "active",
        'contact_us' : contact_us,
        'about' : about,
        'service' : service,
        'detail': detail,
        'currentSite' : currentSite,
        'project' : project,
        'portfolio' : portfolio,
    }
    return render(request, 'pages/index.html', context)
