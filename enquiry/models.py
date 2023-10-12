from django.db import models


STATUS = ((0, "Draft"), (1, "Published"))


class Enquiry(models.Model):
    """ Model for creating/managing enquiries """
    enquiry = models.CharField(max_length=254)
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """ Order Enquiries from newest to oldest """
        ordering = ['-created_on']
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return self.enquiry
