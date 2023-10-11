from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/new_arrivals/', views.new_arrivals, name='new_arrivals'),
    path(
        'products/featured_books/', views.featured_books, name='featured_books'
        ),
    path('products/on_sale/', views.on_sale, name='on_sale'),
    path('products/all_specials/', views.all_specials, name='all_specials'),
    path('products/six_to_eight', views.six_to_eight, name='six_to_eight'),
    path('products/nine_to_ten', views.nine_to_ten, name='nine_to_ten'),
    path('products/eleven_to_twelve',
         views.eleven_to_twelve,
         name='eleven_to_twelve'),
]
