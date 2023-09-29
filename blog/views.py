from django.shortcuts import render


def blog(request):
    """ A view to go to the blog entries """

    return render(request, 'blog/blog.html')
