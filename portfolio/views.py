from django.shortcuts import render

# Create your views here.
def portfolio(request):
    context = {

    }
    return render(request, 'portfolio/portfolio.html', context)

def project(request):
    context = {

    }
    return render(request, 'portfolio/project.html', context)