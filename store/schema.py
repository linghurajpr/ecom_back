import graphene
from graphene_django import DjangoObjectType
from .models import Product, Cart, CartItems

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"

class CartItemType(DjangoObjectType):
    class Meta:
        model = CartItems
        fields = "__all__"

class CartType(DjangoObjectType):
    tot_price = graphene.Float()

    class Meta:
        model = Cart
        fields = "__all__"

    def resolve_tot_price(self, info):
        total = 0
        for item in self.items.all():
            total += item.product.price * item.quantity
        return total

class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    cart = graphene.Field(CartType)

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_cart(self, info):
        cart, created = Cart.objects.get_or_create(id=1)
        return cart

class AddToCart(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int(required=True)

    cart = graphene.Field(CartType)

    def mutate(self, info, product_id):
        product = Product.objects.get(id=product_id)
        cart, _ = Cart.objects.get_or_create(id=1)
        cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
        return AddToCart(cart=cart)

class RemoveFromCart(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int(required=True)

    cart = graphene.Field(CartType)

    def mutate(self, info, product_id):
        cart = Cart.objects.get(id=1)
        try:
            cart_item = CartItems.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
        except CartItems.DoesNotExist:
            pass
        return RemoveFromCart(cart=cart)

class Mutation(graphene.ObjectType):
    add_to_cart = AddToCart.Field()
    remove_from_cart = RemoveFromCart.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
