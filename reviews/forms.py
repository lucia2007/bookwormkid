from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """ Review form """
    class Meta:
        model = Review
        fields = ('body', )
