from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """ A model to add favourite products into a wishlist """
    user_profile = models.ForeignKey(
                                     UserProfile,
                                     on_delete=models.CASCADE,
                                     related_name="customer_wishlist",
                                     default=None
                                    )
    product = models.ForeignKey(
                                Product, on_delete=models.CASCADE, default=None
                                )

    def __str__(self):
        return self.product.title
