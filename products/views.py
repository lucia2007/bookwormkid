from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any keywords.")
                return redirect(reverse('products'))

            # Checks if the search term is either in the title or the descrip.
            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(by_age__icontains=query) | Q(author__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def new_arrivals(request):
    new_arrivals_books = Product.objects.filter(new_arrival=True)

    context = {
        "new_arrivals_books": new_arrivals_books
    }

    return render(request, 'products/new_arrivals.html', context)


def featured_books(request):
    special_feature_books = Product.objects.filter(feature_product=True)

    context = {
        "special_feature_books": special_feature_books
    }

    return render(request, 'products/featured_books.html', context)
