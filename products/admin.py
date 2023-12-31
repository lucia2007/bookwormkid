from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ Product model in Admin """
    list_display = (
        'sku',
        'title',
        'author',
        'category',
        'by_age',
        'price',
        'sale_price',
        'rating',
        'number_of_pages',
        'new_arrival',
        'feature_product',
        'is_sale',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
