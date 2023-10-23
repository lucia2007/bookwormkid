from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """ Class for creating/managing Reviews """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="reviews")
    reviewer = models.ForeignKey(
                                 User,
                                 on_delete=models.CASCADE,
                                 related_name="reviews"
                                 )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"
