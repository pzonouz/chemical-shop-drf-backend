from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer


class FavoriteViewSet(ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user
        favorite = Favorite.objects.filter(
            product_id=request.data.get("product"),
            user=request.data.get("user"),
        ).first()
        if favorite:
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        Favorite.objects.create(
            product_id=request.data.get("product"), user=request.data.get("user")
        )
        return Response(
            status=status.HTTP_201_CREATED,
        )
