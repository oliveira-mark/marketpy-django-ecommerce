from django.shortcuts import render, get_object_or_404
from product.models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product/pages/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product/pages/product.html', {'product': product})