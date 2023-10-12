from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_enquiries, name='enquiries'),
    path('add/', views.add_enquiry, name='add_enquiry'),
]
