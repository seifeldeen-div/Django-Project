from django.shortcuts import render, redirect
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


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']

        Blog.objects.create(
            name=name,
            price=price,
            description=description,
            image=image
        )
        return redirect('blog.index')
    return render(request, 'blog/create.html')