from django import forms
from .models import Article
from .widgets import CustomClearableFileInput


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'image_url', 'image', 'content')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
