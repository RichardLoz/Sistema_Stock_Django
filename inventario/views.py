from django.shortcuts import render, redirect
from .models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products' : products} )


def create_product(request):
    name = request.POST["name"]
    price = request.POST["price"]
    product = Product(name=name, price=price)
    product.save()
    return redirect('/inventario')


def edit_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'edit_product.html', {'product': product})

def update_product(request, id):
    product = Product.objects.get(id=id)
    name = request.POST["name"]
    price = request.POST["price"]
    product.name = name
    product.price = price
    product.save()
    return redirect('/inventario')