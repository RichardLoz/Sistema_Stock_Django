from django.shortcuts import render, redirect
from .models import Product, Category

#TODO: CRUD PRODCUT
def list_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product.html', {'products' : products, 'categories' : categories} )

 
def create_product(request):
    name = request.POST["name"]
    price = request.POST["price"]
    category_id = request.POST["category_id"]
    category = Category.objects.get(id=category_id)
    product = Product(name=name, price=price, category=category)
    product.save()
    return redirect('/inventario')


def edit_product(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    return render(request, 'edit_product.html', {'product': product, 'categories':categories})

def update_product(request, id):
    product = Product.objects.get(id=id)
    name = request.POST["name"]
    price = request.POST["price"]
    category_id = request.POST["category_id"]
    category = Category.objects.get(id=category_id)
    product.name = name
    product.price = price
    product.category = category 
    product.save()
    return redirect('/inventario')

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/inventario/')


#TODO: CRUD CATEGORY
def detail_category(request, id):
    #Filtro
    products = Product.objects.filter(category__id=id) 