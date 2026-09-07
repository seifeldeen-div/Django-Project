from django import forms
from .models import Blog


# class BlogForm(forms.Form):
#     name = forms.CharField(max_length=10, label='Name')
#     price = forms.IntegerField(label='price')
#     description = forms.CharField(max_length=255, label='description', widget=forms.Textarea)
#     image = forms.ImageField(label='image', required=False)


# create model form
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = ['name', 'price', 'description', 'image']
        fields = '__all__'  # get all fields
        # exclude = ['id'] get all data except id
        widgets = {
    'name': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Blog Name'
    }),

    'price': forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Price'
    }),

    'description': forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Blog Description, please',
        'rows': 6
    }),

    'image': forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }),

    'category': forms.Select(attrs={
        'class': 'form-select'
    }),

    'user': forms.Select(attrs={
        'class': 'form-select'
    }),
}

    # validations
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 10:
            raise forms.ValidationError(
                'Name must be at least 10 chars'
            )
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if not description.strip():
            raise forms.ValidationError(
                'Description cannot be empty'
            )
        return description

    # def clean(self):
    #     cleaned_data = super().clean()

    #     name = cleaned_data.get('name', '')
    #     description = cleaned_data.get('description', '')

    #     forbidden_words = ['spam', 'hack', 'badword']

    #     text = f'{name} {description}'.lower()

    #     for word in forbidden_words:
    #         if word in text:
    #             raise forms.ValidationError(
    #                 f'The word "{word}" is not allowed.'
    #             )

    #     return cleaned_data