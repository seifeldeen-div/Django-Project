from django.contrib import admin
from .models import Blog, Profile, User, Tags, Category, Blog_details

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Blog_details)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Tags)
