from django.urls import include, path
from rest_framework.routers import DefaultRouter
from cartItems.views import CartItemViewSet
from categories.views import CategoryAdminViewSet, CategoryListRetrieve

from images.views import ImageUploadView
from orders.views import AdminOrderViewSet, OrderViewSet
from products.views import ProductAdminViewSet, ProductListRetrieve

router = DefaultRouter()
router.register(r"products", ProductListRetrieve, basename="products")
router.register(r"admin/products", ProductAdminViewSet, basename="productsAdmin")
router.register(r"categories", CategoryListRetrieve, basename="categories")
router.register(r"admin/categories", CategoryAdminViewSet, basename="categoriesAdmin")
router.register(r"cart-items", CartItemViewSet, basename="cartItems")
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"admin/orders", AdminOrderViewSet, "ordersAdmin")

urlpatterns = [
    path("auth/", include("auth.urls")),
    path("image-upload/", ImageUploadView.as_view()),
]
urlpatterns = urlpatterns + router.urls
