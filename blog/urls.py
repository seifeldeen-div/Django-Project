from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='blog.index'),
    path("<int:id>/", views.show, name='blog.show')
]
