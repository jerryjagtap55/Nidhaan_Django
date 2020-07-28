from django.shortcuts import render
from contact_us.models import ContactUs
from .models import Project,CurrentSite
# Create your views here.
def index(request):
    contact_us = ContactUs.objects.all()
    project = Project.objects.all()

    context = {
        'contact_us' : contact_us,
        'project' : project,

    }
    return render(request, 'blog/blogs.html', context)

def blog(request):
    contact_us = ContactUs.objects.all()
    context = {
        'contact_us' : contact_us,
    }
    return render(request, 'blog/blog.html', context)

def cs(request):
    contact_us = ContactUs.objects.all()

    context = {
        'contact_us' : contact_us,
    }
    return render(request, 'blog/cs.html', context)