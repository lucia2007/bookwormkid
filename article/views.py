from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Article
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import ArticleForm


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


@login_required
def edit_article(request, slug):
    """ Edit an article """
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.entered_by:
        raise PermissionDenied

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f"Article {article.title} has been updated.")
            return redirect('article_detail', slug=slug)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }

    return render(request, 'article/edit_article.html', context)


@login_required
def delete_article(request, slug):
    """ Delete an article """
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.entered_by:
        messages.error(
            request,
            'Sorry, only the owner of the article can delete their articles.')
        return redirect(reverse('articles'))

    article.delete()
    messages.success(request,
                     f'Article - { article.title } was deleted successfully.')
    return redirect(reverse('articles'))
