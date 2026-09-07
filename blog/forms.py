from django import forms
from .models import Blog


class BlogForm(forms.Form):
    name = forms.CharField(max_length=10, label='Name')
    price = forms.IntegerField(label='price')
    description = forms.CharField(max_length=255, label='description', widget=forms.Textarea)
    image = forms.ImageField(label='image', required=False)


