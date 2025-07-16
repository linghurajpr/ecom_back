import graphene
from graphene_django import DjangoObjectType
from .models import Product ,Cart ,CartItems

class ProductType(DjangoObjectType):
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

class Query(graphene.ObjectType):
    products=graphene.List(ProductType)
    cart=graphene.Field(CartType)

    def res_products(self,info):
        return Product.objects.all()
    
    def res_cart(self,info):
        cart,created=Cart.objects.get_or_create(id=1)
        return cart

Schema=graphene.Schema(query=Query)