from django.db import models


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
    number_of_pages = models.IntegerField()
    description = models.TextField(max_length=1024, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    new_arrival = models.BooleanField(blank=True)
    feature_product = models.BooleanField(blank=True)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
        )
    is_sale = models.BooleanField()
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    ISBN = models.CharField(max_length=13, unique=True)
    by_age= models.CharField(max_length=6, choices=[
        ("6-8", "6-8"), ("9-10", "9-10"), ("11-12", "11-12")])

    def __str__(self):
        return self.title
