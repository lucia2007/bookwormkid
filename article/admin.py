from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin  # type:ignore


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    """ Admin Article Class """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'author', 'status', 'image', 'created_on')
    search_fields = ['title', 'content', 'author']
