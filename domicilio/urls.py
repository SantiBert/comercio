from django.contrib import admin
from django.urls import path
from .views import AdminAddressView, AdminAddressUpdateView

urlpatterns = [
    path('address/show/', AdminAddressView.as_view(), name='address'),
    path('address/update/<int:pk>/',
         AdminAddressUpdateView.as_view(), name='addressUpdate')
]
