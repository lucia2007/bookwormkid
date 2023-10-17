from django.shortcuts import render


def bookstoremanagement(request):
    """ A view to return the bookstoremanagement page """

    return render(request, 'bookstoremanagement/bookstoremanagement.html')


def privacy_policy(request):
    """ A view to return the privacy policy be Termly page """

    return render(request, 'bookstoremanagement/privacy_policy.html')