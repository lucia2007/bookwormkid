from profiles.models import UserProfile
from .models import Wishlist


def wishlist_contents(request):
    """Wishlist contents context processor"""

    if request.user.is_authenticated:
        wishlist_items = []
        user_profile = UserProfile.objects.get(user=request.user)
        wishlist_queryset = Wishlist.objects.filter(user_profile=user_profile)
        # if there are items in the users wishlist
        for item in wishlist_queryset:
            wishlist_items.append(item.product)
    else:
        wishlist_items = []
    return {
        'customer_wishlist': wishlist_items,
    }
