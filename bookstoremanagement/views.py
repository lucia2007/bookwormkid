from django.shortcuts import render


def bookstoremanagement(request):
    """ A view to return the bookstoremanagement page """

    return render(request, 'bookstoremanagement/bookstoremanagement.html')
