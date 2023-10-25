from django.shortcuts import (
                              render,
                              get_object_or_404
                              )
from .models import Review
from .forms import ReviewForm


def review_detail(request, review_id):
    """ A view to show review details. """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
        'review_form': ReviewForm(),
    }

    return render(request, 'review/review_detail.html', context)
