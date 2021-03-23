from django.contrib import admin
from django.urls import path
from .views import SocialListView, SocialUpdateView

urlpatterns = [
    path('social/list/', SocialListView.as_view(), name='socialList'),
    path('social/update/<int:pk>/', SocialUpdateView.as_view(), name='socialUpdate')
]
