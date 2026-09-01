from django.shortcuts import render
from .models import Blog

# Create your views here.


def index(request):
    context = {
        "data": Blog.objects.all()
    }
    return render(request, "blog/index.html", {"context":context})


def show(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/show.html", {"blog": blog})