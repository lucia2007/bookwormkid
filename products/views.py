from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Case, DecimalField, F, Q, Value, When
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review
from reviews.forms import ReviewForm
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None
    current_category = None

    # Product sorting by category, rating and sales price
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('title'))
            if sortkey == "category":
                sortkey = 'category__name'
            # my husband helped me with the sorting price functionality
            # https://docs.djangoproject.com/en/1.8/ref/models/conditional-expressions/#conditional-aggregation
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


@login_required
def product_bought_by_request_user(request, product_id):
    """ Checks if the user bought the book in the past, returns T/F """
    # Get the product instance
    product = get_object_or_404(Product, pk=product_id)

    # Get the user's profile instance
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # Get user's orders
    user_orders = Order.objects.filter(user_profile=user_profile)

    # Check if the product is in any of the user past orders
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
    product_bought = user_orders.filter(lineitems__product=product).exists()

    return product_bought


@login_required
def product_already_reviewed_by_user(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    user_profile = get_object_or_404(UserProfile, user=request.user)

    already_reviewed = Review.objects.filter(
        reviewer=request.user,
        product=product).first()

    return already_reviewed


def product_detail(request, product_id):
    """ A view to show product details. """

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.filter(approved=True).order_by('created_on')
    product_bought = product_bought_by_request_user(request, product_id)
    already_reviewed = product_already_reviewed_by_user(request, product_id)

    context = {
        'product': product,
        'reviews': reviews,
        'reviewed': False,
        'review_form': ReviewForm(),
        'product_bought': product_bought,
        'already_reviewed': already_reviewed
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request, product_id):
    """ Add a new product review """
    """ Only a signed in user can review a product """
    product = get_object_or_404(Product, pk=product_id)

    already_reviewed = product_already_reviewed_by_user(request, product_id)

    if already_reviewed:
        messages.error(
            request,
            'You have already reviewed this book. '
            'You can add only one review per book.')
        return redirect(reverse('product_detail', args=[product_id]))

    reviews = product.reviews.filter(approved=True).order_by('-created_on')

    if not product_bought_by_request_user(request, product_id):
        #  If the user didn't buy the product in the past,
        #  show an error message
        messages.error(
                       request,
                       'You can only leave a review for book '
                       'you bought previously.'
                       )
        return redirect(reverse('product_detail', args=[product_id]))

    product_bought = product_bought_by_request_user(request, product_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review.reviewer = request.user
            review.product = product
            review.save()
            messages.success(request, "Your review is waiting for approval.")
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request,
                           'Review was not added. Correct the form inputs.'
                           )
    else:
        review_form = ReviewForm()

    template = 'product/product_detail.html'
    context = {
        'form': review_form,
        'reviews': reviews,
        'on_page': True,
        'reviewed': True,
        'product_bought': product_bought,
        'already_reviewed': already_reviewed
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a book to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can add book.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Book was added successfully.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Book was not added. Correct the form inputs.'
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
    """ Edit a book in the bookstore offer """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can edit books.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update book. Please check the form inputs.'
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
    """ Delete a book from the store offer """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can delete books.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Book was deleted.')

    context = {
        'on_page': True,
    }

    return redirect(reverse('products'), context)
