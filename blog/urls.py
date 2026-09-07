from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='blog.index'),
    path("<int:id>/", views.show, name='blog.show'),
    path("create/", views.create, name='blog.create'),
    path("<int:id>/edit/", views.edit, name='blog.edit'),
    path("<int:id>/delete/", views.delete, name='blog.delete'),
]
