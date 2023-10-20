from django.shortcuts import (
                              render,
                              get_object_or_404,
                              redirect)
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Review
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReviewForm
from products.models import Product


def review_detail(request, review_id):
    """ A view to show review details. """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
        'review_form': ReviewForm(),
        'commented': False
    }

    return render(request, 'review/review_detail.html', context)

