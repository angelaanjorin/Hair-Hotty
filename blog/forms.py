from .models import Comment, Post
from django import forms
from slugify import slugify
from django_summernote.widgets import SummernoteWidget
from cloudinary.forms import CloudinaryInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ Form to create a Post"""
    title = forms.CharField(max_length=200)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Set the slug value from the title
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Post Title",
            "featured_image": "Post Image",
            "content": "Content",
        }