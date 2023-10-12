""" faq admin"""
from django.contrib import admin
from .models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    """ Enquiry model display """
    list_display = (
        'enquiry', 'answer', 'status', 'created_on'
    )

    search_fields = ('enquiry', 'answer')
    ordering = ('created_on',)


admin.site.register(Enquiry, EnquiryAdmin)