from .models import Enquiry
from django import forms

STATUS = ((0, 'Draft'), (1, 'Published'))


class EnquiryForm(forms.ModelForm):
    """ Form to create/edit an enquiry """
    class Meta:
        """ Enquiry form"""
        model = Enquiry
        fields = '__all__'
