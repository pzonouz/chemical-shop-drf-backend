from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from categories.models import Category
from categories.serializers import CategoryAdminSerializer, CategorySerializer


class CategoryListRetrieve(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryAdminSerializer
