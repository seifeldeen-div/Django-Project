from django.shortcuts import render


# Create your views here. >> logic

def index(request):
    context = {'title': 'Home'}
    return render(request, "home/index.html", {'context': context})


def about(request):
    context = {'title': 'About'}
    return render(request, 'home/about.html', {'context': context})