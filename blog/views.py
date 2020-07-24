from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'blog/blogs.html', context)

def blog(request):
    context = {

    }
    return render(request, 'blog/blog.html', context)

def cs(request):
    context = {

    }
    return render(request, 'blog/cs.html', context)