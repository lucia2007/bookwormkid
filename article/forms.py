from .models import Article
from slugify import slugify  # type:ignore
from django import forms
from djrichtextfield.widgets import RichTextWidget
from .widgets import CustomClearableFileInput

STATUS = ((0, 'Draft'), (1, 'Published'))


class ArticleForm(forms.ModelForm):
    """ Form to create/edit an article """
    title = forms.CharField(max_length=200)
    excerpt = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    content = forms.CharField(widget=RichTextWidget())
    status = forms.ChoiceField(
        choices=STATUS, required=True, widget=forms.RadioSelect())

    class Meta:
        model = Article
        fields = [
                 'title',
                 'author',
                 'image',
                 'image_description',
                 'excerpt',
                 'content',
                 'status',
                 'source']
        content = forms.CharField(widget=RichTextWidget())
        labels = {
            'title': 'Article Title',
            'author': 'Article Author',
            'image': 'Image Upload',
            'image_description': 'Describe Image',
            'excerpt': 'Excerpt',
            'content': 'Content',
            'status': 'Status',
            'source': 'Source'
        }

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
