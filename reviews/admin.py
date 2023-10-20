""" Reviews Admin """
from django.contrib import admin
from .models import Review
from django.contrib.auth.models import User


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Review model display """
    list_display = (
        'name', 'body', 'product', 'created_on', 'approved', 'reviewer'
    )
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_reviews']
    ordering = ('created_on',)

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
