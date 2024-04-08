# type:ignore
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db import transaction

from cartItems.models import CartItem
from cartItems.serializers import CartItemSerializerForOrder
from orders.models import Order
from users.serializers import CustomUserSerializer
from processes.serializers import ListProcessSerializer


class OrderSerializer(ModelSerializer):
    cart_items = CartItemSerializerForOrder(many=True)
    pk = serializers.IntegerField(required=False)
    processes = ListProcessSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "pk",
            "id",
            "cart_items",
            "processes",
            "created_at",
            "delivery_method",
        )
        read_only_fields = ("processes",)

    def save(self, **kwargs):
        with transaction.atomic():
            order = Order.objects.create(
                # user=self.validated_data.get("user"),
                user=self.context.get("request").user,
                delivery_method=self.validated_data.get("delivery_method"),
            )
            cart_items = self.validated_data.get("cart_items")
            for item in cart_items:
                cart_item = CartItem.objects.get(pk=item.get("pk"))
                cart_item.order = order
                cart_item.save()


class OrderAdminSerializer(ModelSerializer):
    cart_items = CartItemSerializerForOrder(many=True)
    user = CustomUserSerializer()
    pk = serializers.IntegerField(required=False)
    processes = ListProcessSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
