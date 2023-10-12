from django.shortcuts import (
                              render,
                              get_object_or_404,
                              reverse,
                              redirect)
from django.urls import reverse_lazy
from .models import Article
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import ArticleForm


def all_articles(request):
    """ A view to return all articles """
    articles = Article.objects.all().filter(status=1)

    context = {
        'articles': articles,
    }

    return render(request, 'article/articles.html', context)


def article_detail(request, slug, *args, **kwargs):
    """ A view to show article details. """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)

    liked = False

    if article.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'article': article,
        'liked': liked,
    }

    return render(request, 'article/article_detail.html', context)


@login_required
def add_article(request):
    """ Add a new article """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can add new articles.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, "Article was added successfully.")
            return redirect(reverse_lazy('article_detail', args=[article.slug]))
        else:
            messages.error(request,
                           'Article was not added. Correct the form inputs.'
                           )
    else:
        form = ArticleForm()

    template = 'article/add_article.html'
    context = {
        'form': form,
        'on_page': True
    }

    return render(request, template, context)

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
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
        'on_page': True,
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

    context = {
        'on_page': True,
    }

    return redirect(reverse('articles'), context)


@login_required
def like_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))
