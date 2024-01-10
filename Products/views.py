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

def update_products(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product_name = request.POST.get('name')
        product_qtty = request.POST.get('qtty')
        product_price = request.POST.get('price')
        product_desc = request.POST.get('desc')
        product_image = request.FILES.get('image')
        product.name = product_name
        product.qtty = product_qtty
        product.price = product_price
        product.image = product_image
        product.desc = product_desc
        product.save()
        messages.success(request, 'Product saved successfully')
        return redirect('products-url')
    return render(request, 'Products/update-products.html', {'product':product})


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('products-url')


def pay(request, id):
    product =Product.objects.get(id=id)
    return render(request, 'Products/pay.html', {'product':product})