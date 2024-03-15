from rest_framework.serializers import ModelSerializer

from cartItems.models import CartItem

# from products.serializers import ProductSerializer


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("user", "product", "quantity", "pk")
