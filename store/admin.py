from django.contrib import admin
from .models import Product ,Cart,CartItems

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','category','price','in_stock']
    search_fields=['name','category']
    list_display=['category','instock']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'in_stock']
    search_fields = ['name', 'category']
    list_filter = ['category', 'in_stock']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    date_hierarchy = 'created'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']
    list_filter = ['product']