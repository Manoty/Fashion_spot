from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from .models import Product
import json
from django.views.decorators.csrf import csrf_exempt

from .credentials import *
from django.http import HttpResponse



# Create your views here.
def Products(request):
    all_products = Product.objects.all()
    context = {"products":all_products}
    return render(request, 'Products/products.html', context)

@login_required
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
@login_required
def update_products(request, id):
    product = Product.objects.get(id=id)
    '''
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
        '''
    return render(request, 'Products/update-products.html', {'product':product})

@login_required
def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('products-url')

@login_required
def pay(request, id):
    product =Product.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST['phone']
        amount = product.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "School fees"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("success")
    return render(request, 'Products/pay.html', {'product':product})

def mpesa_callback(request):
    if request.method == 'POST':
        # GET CALLBACK DATA FROM MPESA
        callback_data = json.loads(request.body.decode('utf-8'))

        # Process the  Mpesa callback data
        transaction_status = callback_data.get('Body',{}).get('stkCallback',{}).get('ResultCode')

        # Update database or send notificationbased on the transaction status
        if transaction_status == 0:
            #successful transaction
            #update database / send notification
            print('Notification: Payment successful.Transaction details:',callback_data)
        else:
            #failed transaction
            #handle failure, update database
            print('Notification: Payment failed.Transaction details:', callback_data)
        response_data = {
            "ResultCode":0,
            "ResultDesc": 'Success',
        }
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    return HttpResponse(status=405)