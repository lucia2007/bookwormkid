from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Case, DecimalField, F, Q, Value, When
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review
from reviews.forms import ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None
    current_category = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('title'))
            if sortkey == "category":
                sortkey = 'category__name'
            # https://docs.djangoproject.com/en/1.8/ref/models/conditional-expressions/#conditional-aggregation
            # my husbang helped me with the sorting price functionality
            if sortkey == "price":
                sortkey = 'sort_price'
                products = products.annotate(sort_price=Case(
                    When(Q(is_sale=True) & Q(sale_price__isnull=False),
                         then='sale_price'),
                    default='price',
                    output_field=DecimalField()))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            current_category = Category.objects.get(name=category)
            products = products.filter(category__name=category)

        if 'age' in request.GET:
            age = request.GET['age']
            products = products.filter(by_age=age)

        if 'new' in request.GET:
            new = request.GET['new']
            products = products.filter(new_arrival=True)

        if 'sale' in request.GET:
            sale = request.GET['sale']
            products = products.filter(is_sale=True)
            products_on_sale = products

            context = {
                'products_on_sale': products_on_sale
            }

        if 'featured' in request.GET:
            featured = request.GET['featured']
            products = products.filter(feature_product=True)

        if 'specials' in request.GET:
            criteria = Q(new_arrival=True) | Q(feature_product=True) | Q(
                is_sale=True)
            specials = request.GET['specials']
            products = products.filter(criteria)

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
        'current_category': current_category,
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
