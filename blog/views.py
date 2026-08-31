from django.shortcuts import render

# Create your views here.
data = [
    {
        'id': 1,
        'name': 'FaceBook',
        'price': 12,
        'description': 'A mind-bending heist thriller.',
        'url': 'img/facebook.jpg'
    },
    {
        'id': 2,
        'name': 'Twitter',
        'price': 13,
        'description': 'A journey to a distant world',
        'url': 'img/twitter.jpg'
    },
]


def index(request):
    context = {
        "data": data
    }
    return render(request, "blog/index.html", {"context":context})


def show(request, id):
    blog = data[id - 1]
    return render(request, "blog/show.html", {"blog": blog})