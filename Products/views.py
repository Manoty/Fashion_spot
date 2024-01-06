from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from .models import Product

# Create your views here.
def Products(request):
    all_products = Product.objects.all()
    context = {"products":all_products}
    return render(request, 'Products/products.html', context)


def add_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved Successfully')
            return redirect('add-products-url')


    else:
        form = ProductForm()
    return render(request, 'Products/add-products.html', {'form':form})

def update_products(request):
    return render(request, 'Products/update-products.html')


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('products-url')