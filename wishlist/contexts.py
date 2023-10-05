from profiles.models import UserProfile
from .models import Wishlist


def wishlist_contents(request):
    """Wishlist contents context processor"""
    wishlist_contents = []

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        wishlist_items = Wishlist.objects.filter(user_profile=user_profile)

    context = {
        'customer_wishlist': wishlist_items,
    }

    return context
