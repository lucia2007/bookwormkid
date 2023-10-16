from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path(
        'products/featured_books/', views.featured_books, name='featured_books'
        ),
    path('products/on_sale/', views.on_sale, name='on_sale'),
    path('products/all_specials/', views.all_specials, name='all_specials'),
]
