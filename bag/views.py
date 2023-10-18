from django.shortcuts import (
                             render,
                             redirect,
                             get_object_or_404
                             )
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to return the page with bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the amnount of the chosen product into the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'You have updated {product.title} quantity to {bag[item_id]}'
            )
    else:
        bag[item_id] = quantity
        messages.success(
            request,
            f'You have successfully added { product.title } to your bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the amnount of the chosen product in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'You have updated {product.title} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(
            request,
            f'{product.title} was removed from your shopping bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the chosen product from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(
            request,
            f'{product.title} was removed from your shopping bag.')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error when removing item: {e}')
        return HttpResponse(status=500)
