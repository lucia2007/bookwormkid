from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    """ Form to create/edit an article """
    class Meta:
        model = Article
        fields = '__all__'
