from django.contrib import admin
from .models import Product, Cart, CartItems

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItems)
