from django.shortcuts import render
from blog.models import Blog

# Create your views here.

def index(request):
    blogs = {
        "blogs" : Blog.objects.all()
    }
    return render(request, "orm_test/index.html", blogs)