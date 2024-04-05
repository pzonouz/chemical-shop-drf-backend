from django.urls import include, path
from rest_framework.routers import DefaultRouter
from cartItems.views import CartItemViewSet
from categories.views import CategoryAdminViewSet, CategoryListRetrieve

from images.views import ImageUploadView
from orders.views import OrderAdminViewSet, OrderViewSet
from processes.views import ProcessViewSet
from products.views import ProductAdminViewSet, ProductListRetrieve
from users.views import UserAdminViewSet
from favorites.views import FavoriteViewSet

router = DefaultRouter()
router.register(r"products", ProductListRetrieve, basename="products")
router.register(r"admin/products", ProductAdminViewSet, basename="productsAdmin")
router.register(r"categories", CategoryListRetrieve, basename="categories")
router.register(r"admin/categories", CategoryAdminViewSet, basename="categoriesAdmin")
router.register(r"cart-items", CartItemViewSet, basename="cartItems")
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"admin/orders", OrderAdminViewSet, basename="ordersAdmin")
router.register(r"admin/users", UserAdminViewSet, basename="usersAdmin")
router.register(r"admin/processes", ProcessViewSet, basename="processesAdmin")
router.register(r"favorites", FavoriteViewSet, basename="favorites")

urlpatterns = [
    path("auth/", include("auth.urls")),
    path("image-upload/", ImageUploadView.as_view()),
]
urlpatterns = urlpatterns + router.urls
