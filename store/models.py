from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=56)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    instock=models.BooleanField(default=True)

class Cart(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cart{self.id}-Created on {self.create}"
    
class CartItems(models.Model):
    cart=models.ForeignKey(Cart,related_name='items',on_delete=models.CASCADE)
    prod=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x{self.prod.name}"