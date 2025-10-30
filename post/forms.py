from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']  # अपने model के fields के हिसाब से
