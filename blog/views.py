from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.


def index(request):
    context = {
        "data": Blog.objects.all()
    }
    return render(request, "blog/index.html", {"context":context})


def show(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/show.html", {"blog": blog})


# def create(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         price = request.POST['price']
#         description = request.POST['description']
#         image = request.FILES['image']

#         Blog.objects.create(
#             name=name,
#             price=price,
#             description=description,
#             image=image
#         )
#         return redirect('blog.index')
#     return render(request, 'blog/create.html')
# ---------------------------------------------------------------------------------------
# def create(request):
#     data = {}

#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             Blog.objects.create(
#                 name = form.cleaned_data['name'],
#                 price = form.cleaned_data['price'],
#                 description = form.cleaned_data['description'],
#                 image = form.cleaned_data['image']
#             )
#             return redirect('blog.index')

#     else:
#         form = BlogForm()

#     data['form'] = form
#     return render(request, 'blog/create2.html', {'data' : data })
# ----------------------------------------------------------------------------------------
def create(request):
    data = {}
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog.index')
    else:
        form = BlogForm()
    data['form'] = form
    return render(request, 'blog/create3.html', {'data': data})


# Editing Blog
def edit(request,id):
    blog = Blog.objects.get(id=id)
    data = {}
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance= blog)
        if form.is_valid():
            form.save()
        return redirect('blog.show', id=id)
    else:
        form = BlogForm(instance= blog)
        data['form'] = form
    return render(request, 'blog/edit.html', {"data":data})

# delete Blog
def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blog.index')