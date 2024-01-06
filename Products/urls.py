from django.urls import path
from . import views as my_views

urlpatterns = [

    path('', my_views.Products, name='products-url'),
    path('add-products/', my_views.add_products, name='add-products-url')
    path('delete/<id>', my_views.delete, name='delete-url'),
]