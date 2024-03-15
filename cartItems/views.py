from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from cartItems.models import CartItem
from cartItems.serializers import CartItemSerializer


class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        print(self.request.user)
        return CartItem.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = {**request.data, "user": user.id}
        print(data)
        (cartItem, created) = CartItem.objects.get_or_create(user=user)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        if data.product in cartItem.products:
            print(cartItem)

        # headers = self.get_success_headers(serializer.data)
        return Response(
            ""
            # serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
