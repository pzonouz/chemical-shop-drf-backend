from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


from cartItems.models import CartItem
from cartItems.serializers import CartItemSerializer


class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data
        data["user"] = user.id
        try:
            existingCartItem = CartItem.objects.get(
                user__id=data["user"], product__id=data["product"]
            )
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            existingCartItem.quantity = existingCartItem.quantity + data["quantity"]
            existingCartItem.save()
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        except ObjectDoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
