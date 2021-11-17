from django.urls import path
from products.views import products

urlpatterns = [
    path('list/', products.list, name='list-product'),
    path('create/', products.create, name='create-product'),
    path('edit/<int:product_id>/', products.edit, name='edit-product'),
]