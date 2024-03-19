from rest_framework.serializers import ModelSerializer

# from cartItems.serializers import CartItemSerializer
from orders.models import Order


class OrderSerializer(ModelSerializer):
    # cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "user", "cart_items", "delivery_method")
