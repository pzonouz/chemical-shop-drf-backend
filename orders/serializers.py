from rest_framework.serializers import ModelSerializer

from cartItems.serializers import CartItemSerializerForOrder
from orders.models import Order
from users.serializers import CustomUserSerializer


class OrderSerializer(ModelSerializer):
    user = CustomUserSerializer()
    cart_items = CartItemSerializerForOrder(many=True)

    class Meta:
        model = Order
        fields = ("id", "user", "cart_items", "delivery_method")
