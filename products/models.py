from django.db import models
# https://github.com/worldofmarcus/project-portfolio-5/blob/main/products/models.py
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Category Models"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    RELUCTANT = 'reluctant'
    KEEN = 'keen'
    AVID = 'avid'

    CATEGORY_CHOICES = [
        (RELUCTANT, 'reluctant'),
        (KEEN, 'keen'),
        (AVID, 'avid'),
    ]

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        " Method to return category's friendly name "
        return self.friendly_name


class Product(models.Model):
    """ Model for children's books """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    size = models.CharField(max_length=254)
    number_of_pages = models.PositiveIntegerField()
    description = models.TextField(max_length=1024, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
            MinValueValidator(0.0, message=None)])
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, validators=[
            MinValueValidator(0.0, message=None)])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    new_arrival = models.BooleanField(blank=True)
    feature_product = models.BooleanField(blank=True)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
        )
    is_sale = models.BooleanField()
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, validators=[
            MinValueValidator(0.0, message=None)])
    ISBN = models.CharField(max_length=13, unique=True)
    by_age = models.CharField(max_length=6, choices=[
        ("6-8", "6-8"), ("9-10", "9-10"), ("11-12", "11-12")])

    # https://www.andreadiotallevi.com/blog/how-to-use-the-property-decorator-in-python-and-django
    # To be able to user final_price as model attribute
    # without having to add a new model field
    @property
    def final_price(self):
        """ If product is on sale, set it's sales price to final price """
        products = Product.objects.all()
        for product in products:
            try:
                if self.is_sale and self.sale_price < self.price:
                    return self.sale_price
                else:
                    return self.price
            except (TypeError, ValueError):
                return None

    def __str__(self):
        return self.title
