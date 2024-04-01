from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from cartItems.models import CartItem
from cartItems.serializers import CartItemSerializerForOrder
from orders.models import Order
from orders.serializers import OrderAdminSerializer, OrderSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    class Mate:
        model = Order

    def create(self, request, *args, **kwargs):
        user_id = self.request.user.pk
        # user_qs = CustomUser.objects.filter(pk=user_id).first()
        # userSerializer = CustomUserSerializer(user_qs)
        data = request.data
        data["user"] = user_id
        cart_items_qs = CartItem.objects.prefetch_related("product").filter(
            user__id=user_id, order=None
        )
        data["cart_items"] = []
        for item in cart_items_qs:
            data["cart_items"].append(CartItemSerializerForOrder(item).data)

        if data["cart_items"] == []:
            return Response("Cart Items is empty", status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class OrderAdminViewSet(
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAdminUser]
    serializer_class = OrderAdminSerializer

    def get_queryset(self):
        return Order.objects.prefetch_related("cart_items").select_related("user").all()

    class Meta:
        model = Order
