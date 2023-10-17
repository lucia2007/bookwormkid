from django.shortcuts import render


def bookstoremanagement(request):
    """ A view to return the bookstoremanagement page """

    context = {
        'on_page': True,
    }

    return render(
                  request,
                  'bookstoremanagement/bookstoremanagement.html',
                  context)


def privacy_policy(request):
    """ A view to return the privacy policy be Termly page """

    return render(request, 'bookstoremanagement/privacy_policy.html')


def terms_and_conditions(request):
    """ A view to return the terms_and_conditions be Termly page """

    return render(request, 'bookstoremanagement/terms_and_conditions.html')
