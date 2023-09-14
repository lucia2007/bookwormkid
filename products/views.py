from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('title'))
            if sortkey == "category":
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

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
            queries = Q(title__icontains=query) | Q(
                description__icontains=query
                ) | Q(
                by_age__icontains=query
                ) | Q(
                    author__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


def on_sale(request):
    on_sale_books = Product.objects.filter(is_sale=True)

    context = {
        "on_sale_books": on_sale_books
    }

    return render(request, 'products/on_sale.html', context)


def all_specials(request):
    criteria = Q(new_arrival=True) | Q(feature_product=True) | Q(is_sale=True)

    all_specials_books = Product.objects.filter(criteria)

    context = {
        "all_specials_books": all_specials_books
    }

    return render(request, 'products/all_specials.html', context)
