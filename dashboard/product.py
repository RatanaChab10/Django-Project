from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from .models import Category,Product
from django.core.exceptions import RequestAborted
from django.views.decorators.http import require_GET , require_POST 
import os
from datetime import datetime
from django.db import IntegrityError

@require_GET
def index(request):
    products = Product.objects.all()
    return render(request,'product/view.html',{'products':products})

@require_GET
def create(request):
    category = Category.objects.all()
    return render(request,'product/create.html',{'category':category})

@require_POST
def store_product(request):
    try:
        product = Product()
        product.name = request.POST["name"]
        product.barcode = request.POST["barcode"]
        product.unitprice = request.POST["unitprice"]
        product.qtyInstock = request.POST["instock"]
        product.photo = request.FILES['photo']
        product.category_id = request.POST['selectitem']
        product.create_by = 1
        product.save()
        messages.success(request,"Product Created.")
        return redirect('/product_table')
    except Exception as e:
        print("Error:" + str(e))
    return render(request,'product/create.html')

@require_GET
def view_product(request,id):
    try:
        product_view = Product.objects.get(id=id)
    except Exception as e:
        print("Error:" + str(e))
    return render(request,'product/view_product.html',{'product_view':product_view})

@require_GET
def edit_product(request,id):
    product_view = Product.objects.get(id=id)
    category = Category.objects.all()
    return render(request,'product/update_product.html',{'product_view':product_view,'category':category})

@require_POST
def update_product(request,id):
    if request.user.is_authenticated == 1:
        product = Product.objects.get(id=id)
        try:
            if request.method == 'POST':
                product.name = request.POST['name']
                product.barcode = request.POST["barcode"]
                product.unitprice = request.POST["unitprice"]
                product.qtyInstock = request.POST["instock"]
                product.Category = request.POST['selectitem']
                product.update_date = datetime.now()
                if len(request.FILES) != 0:
                    if len(product.photo) > 0:
                        os.remove(product.photo.path)
                    product.photo = request.FILES['photo']
            product.save()
            messages.success(request,"Product Updated.")
            return redirect('/product_table')
        except IntegrityError as e:
            print("Error:" + str(e))
            messages.warning(request,str(e))
    else:
        messages.success(request,"No Permission")
    return redirect('/product_table')
    

    