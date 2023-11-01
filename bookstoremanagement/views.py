from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.contrib import messages


@login_required
def bookstoremanagement(request):
    """ A view to return the bookstoremanagement page """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only a store admin can access this link.')
        return redirect(reverse('home'))
    else:
        return render(
                  request,
                  'bookstoremanagement/bookstoremanagement.html',
                  )


def privacy_policy(request):
    """ A view to return the privacy policy be Termly page """

    return render(request, 'bookstoremanagement/privacy_policy.html')


def terms_and_conditions(request):
    """ A view to return the terms_and_conditions be Termly page """

    return render(request, 'bookstoremanagement/terms_and_conditions.html')
