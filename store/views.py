from django.shortcuts import render, get_object_or_404
from product.models import Product

def product_list(request):
    products = Product.objects.all()
    title_page = "Products List"
    return render(request, 'store/product/pages/product_list.html', {'products': products, 'title_page': title_page})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    title_page = product.name
    return render(request, 'store/product/pages/product.html', {'product': product, 'title_page': title_page})

def checkout(request):
    products = Product.objects.all()
    title_page = "Checkout"
    return render(request, 'store/global/pages/checkout.html', {'products': products, 'title_page': title_page})

def shopping_cart(request):
    products = Product.objects.all()
    title_page = "Shopping Cart"
    return render(request, 'store/global/pages/shopping_cart.html', {'products': products, 'title_page': title_page})

def support(request):
    title_page = "Support"
    return render(request, 'store/global/pages/support.html', {'title_page': title_page})

def my_profile(request):
    title_page = "My Profile"
    return render(request, 'store/user-account/pages/profile.html', {'title_page': title_page})

def my_purchases(request):
    title_page = "My Purchases"
    return render(request, 'store/user-account/pages/my_purchases.html', {'title_page': title_page})

def wishlist(request):
    products = Product.objects.all()
    title_page = "Wishlist"
    return render(request, 'store/user-account/pages/wishlist.html', {'products': products, 'title_page': title_page})

def account_settings(request):
    title_page = "Account Settings"
    return render(request, 'store/user-account/pages/account_settings.html', {'title_page': title_page})

def home(request):
    products = Product.objects.all()
    title_page = "Home"
    return render(request, 'store/global/pages/home.html', {'products': products, 'title_page': title_page})