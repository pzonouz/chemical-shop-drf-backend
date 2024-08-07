from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from auth.views import AuthActivation
from config import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/auth/activate/<uid>/<token>/", AuthActivation.as_view()),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    # path("api/auth/", include("djoser.social.urls")),
]
urlpatterns = urlpatterns + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
