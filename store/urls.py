from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('support/', views.support, name='support'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('my-purchases/', views.my_purchases, name='my_purchases'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('', views.home, name='home'),
]