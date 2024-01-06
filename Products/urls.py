from django.urls import path
from . import views as my_views

urlpatterns = [

    path('', my_views.Products, name='products-url'),
    path('add-products/', my_views.add_products, name='add-products-url'),
    path('delete/<id>', my_views.delete, name='delete-url'),
    path('update/<id>', my_views.update_products, name='update-products-url'),
]