from django.shortcuts import render


def view_bag(request):
    """ A view to return the page with bag contents """

    return render(request, 'bag/bag.html')
