from rest_framework.routers import DefaultRouter
from categories.views import CategoryAdminViewSet, CategoryListRetrieve

from products.views import ProductAdminViewSet, ProductListRetrieve

router = DefaultRouter()
router.register(r"products", ProductListRetrieve, basename="products")
router.register(r"admin/products", ProductAdminViewSet, basename="productsAdmin")
router.register(r"categories", CategoryListRetrieve, basename="categories")
router.register(r"admin/categories", CategoryAdminViewSet, basename="categoriesAdmin")


urlpatterns = router.urls