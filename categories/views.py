from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListRetrieve(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAdminViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
