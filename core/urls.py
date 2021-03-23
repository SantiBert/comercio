from django.urls import path
from .views import IndexView, AdministrationView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('administration/', AdministrationView.as_view(), name="administration"),
]
