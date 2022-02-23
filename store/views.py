from math import prod

from django.shortcuts import get_object_or_404, render

from store.models import Category, Product


def all_products(request):
    products = Product.products.all()
    return render(request,'store/home.html',{'products':products})


def single_product(request,slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request,'store/products/single_product.html',{'product':product})

def category_list(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category':category,'products':products})