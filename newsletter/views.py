from django.shortcuts import render


def newsletter(request):
    """ A view to return the newsletter page """
    return render(request, 'newsletter/newsletter.html')
