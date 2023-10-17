from django.urls import path
from . import views


urlpatterns = [
    path('bookstoremanagement', views.bookstoremanagement, name="bookstoremanagement"),
    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
]
