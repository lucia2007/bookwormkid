from django.shortcuts import (render,
                              redirect,
                              reverse,
                              HttpResponse,
                              get_object_or_404)
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """ A view to go to their wishlist entries """

    user_profile = UserProfile.objects.get(user=request.user)
    customer_wishlist = Wishlist.objects.filter(user_profile=user_profile)

    context = {
        'customer_wishlist': customer_wishlist
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ Add the chosen product into the wishlist """

    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if Wishlist.objects.filter(
                               user_profile=user_profile,
                               product=product).exists():
        messages.warning(
                         request,
                         f'You already have { product.title } in your wishlist.')
        return redirect(reverse('products'))
    else:
        wishlist_item = Wishlist.objects.create(
                                                user_profile=user_profile,
                                                product=product
                                                )
        messages.success(
                         request,
                         f'You have successfully added { wishlist_item.product.title } to your wishlist.'
                         )
        return redirect(reverse('wishlist'))


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove the chosen product from the wishlist """

    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(
                                         user_profile=user_profile,
                                         product=product
                                         )
    wishlist_item.delete()
    messages.success(
                        request,
                        f'{product.title} was successfully removed from your wishlist.'
                        )
    return redirect(reverse('wishlist'))
