from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Article
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# def blog(request):
#     """ A view to go to the blog entries """

#     return render(request, 'blog/blog.html')


def all_articles(request):
    """ A view to return all articles """
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'article/articles.html', context)


def article_detail(request, article_id):
    """ A view to show article details. """

    article = get_object_or_404(article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/article_detail.html', context)
