from django.shortcuts import render, get_object_or_404
from product.models import Product

def product_list(request):
    title_page = "Products List"
    products = Product.objects.all()
    return render(request, 'store/product/pages/product_list.html', {'products': products, 'title_page': title_page})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    title_page = product.name
    return render(request, 'store/product/pages/product.html', {'product': product, 'title_page': title_page})