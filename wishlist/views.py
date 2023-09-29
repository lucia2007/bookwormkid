from django.shortcuts import render


def wishlist(request):
    """ A view to go to their wishlist entries """

    return render(request, 'wishlist/wishlist.html')
