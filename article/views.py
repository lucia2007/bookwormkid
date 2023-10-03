from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Article
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


def all_articles(request):
    """ A view to return all articles """
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'article/articles.html', context)


def article_detail(request, slug):
    """ A view to show article details. """

    article = get_object_or_404(Article, slug=slug)

    context = {
        'article': article,
    }

    return render(request, 'article/article_detail.html', context)
