from django.urls import path
from . import views

urlpatterns = [
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('add/', views.add_review, name='add_review'),
]
