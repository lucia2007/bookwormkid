from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_enquiries, name='enquiries'),
    path('add/', views.add_enquiry, name='add_enquiry'),
    path('edit/<int:enquiry_id>/', views.edit_enquiry, name='edit_enquiry'),
    path(
        'delete/<int:enquiry_id>/',
        views.delete_enquiry,
        name='delete_enquiry'),
]
