from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin_product.js',)

admin.site.register(Product, ProductAdmin)

