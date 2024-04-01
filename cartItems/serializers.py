from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from cartItems.models import CartItem
from products.serializers import ProductSerializer


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = "__all__"


class CartItemSerializerForOrder(ModelSerializer):
    pk = serializers.IntegerField(required=False)
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"
