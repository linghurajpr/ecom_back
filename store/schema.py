import graphene
from graphene_django import DjangoObjectType
from .models import Product ,Cart ,CartItems

class Product(DjangoObjectType):
   class meta:
      model=Product

class CartItemType(DjangoObjectType):
   class meta:
      model=CartItems

class CartType(DjangoObjectType):
    class Meta:
        model=Cart
    
    tot_price=graphene.Float()
   
    def res_tot_price(self,info):
        tot=0
        for item in self.items.all():
            tot+=item.product.price * item.quantity
        return tot
