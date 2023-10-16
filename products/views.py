from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

from .forms import ProductForm


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

        if 'age' in request.GET:
            age = request.GET['age']
            products = products.filter(by_age=age)

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


def nine_to_ten(request):
    """ A view to return the 6-8 page """
    nine_to_ten = Product.objects.filter(by_age='9-10')
    categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    context = {
        'nine_to_ten': nine_to_ten,
        'current_categories': categories,
    }

    return render(request, 'products/nine_to_ten.html', context)


def eleven_to_twelve(request):
    """ A view to return the 6-8 page """
    eleven_to_twelve = Product.objects.filter(by_age='11-12')
    categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    context = {
        'eleven_to_twelve': eleven_to_twelve,
        'current_categories': categories,
    }

    return render(request, 'products/eleven_to_twelve.html', context)


def new_arrivals(request):
    """ Display all new arrivals """
    new_arrivals_books = Product.objects.filter(new_arrival=True)

    context = {
        "new_arrivals_books": new_arrivals_books
    }

    return render(request, 'products/new_arrivals.html', context)


def featured_books(request):
    """ Display special feature books """
    special_feature_books = Product.objects.filter(feature_product=True)

    context = {
        "special_feature_books": special_feature_books
    }

    return render(request, 'products/featured_books.html', context)


def on_sale(request):
    """ Display books which are on sale """
    on_sale_books = Product.objects.filter(is_sale=True)

    context = {
        "on_sale_books": on_sale_books
    }

    return render(request, 'products/on_sale.html', context)


def all_specials(request):
    """ Display all specials (new arrivals, featured, sale) """
    criteria = Q(new_arrival=True) | Q(feature_product=True) | Q(is_sale=True)

    all_specials_books = Product.objects.filter(criteria)

    context = {
        "all_specials_books": all_specials_books
    }

    return render(request, 'products/all_specials.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can add products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Product was added successfully.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Product was not added. Correct the form inputs.'
                           )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'on_page': True,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the bookstore offer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can edit products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please check the form inputs.'
                          )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'on_page': True,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store offer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product was deleted.')

    context = {
        'on_page': True,
    }

    return redirect(reverse('products'), context)
