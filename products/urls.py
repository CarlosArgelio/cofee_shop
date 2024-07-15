from django.urls import path

from .views import ProductListView, ProductFormView, ProductListAPI

urlpatterns = [
    path('', ProductListView.as_view(), name="list_product"),
    path('api/', ProductListAPI.as_view(), name="list_product_api"),
    path('add/', ProductFormView.as_view(), name="add_product"),
]
