from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cartItems.views import CartItemViewSet
from categories.views import CategoryAdminViewSet, CategoryListRetrieve
from favorites.views import FavoriteViewSet
from images.views import ImageUploadView
from orders.views import OrderAdminViewSet, OrderViewSet
from processes.views import ProcessViewSet
from products.views import ProductAdminViewSet, ProductListRetrieve
from store.views import StoreViewSet
from users.views import UserProfileAdminViewSet, UserProfileViewSet

router = DefaultRouter()
router.register("products", ProductListRetrieve, basename="products")
router.register("admin/products", ProductAdminViewSet, basename="productsAdmin")
router.register("admin/processes", ProcessViewSet, basename="processesAdmin")
router.register("admin/categories", CategoryAdminViewSet, basename="categoriesAdmin")
router.register("categories", CategoryListRetrieve, basename="categories")
router.register("admin/orders", OrderAdminViewSet, basename="ordersAdmin")
router.register("admin/user_profiles", UserProfileAdminViewSet, basename="usersAdmin")
router.register("cart-items", CartItemViewSet, basename="cartItems")
router.register("orders", OrderViewSet, basename="orders")
router.register("user_profiles", UserProfileViewSet, basename="users")
router.register("favorites", FavoriteViewSet, basename="favorites")
router.register("store", StoreViewSet, basename="store")

urlpatterns = [
    path("auth/", include("auth.urls")),
    path("image-upload/", ImageUploadView.as_view()),
    path("statuses/", include("orders.urls")),
]
urlpatterns = urlpatterns + router.urls
