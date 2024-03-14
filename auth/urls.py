from django.urls import path, re_path

from auth.views import CustomProviderAuthView, LoginView


urlpatterns = [
    path("login", LoginView.as_view()),
    re_path(
        r"^o/(?P<provider>\S+)/$",
        CustomProviderAuthView.as_view(),
        name="provider-auth",
    ),
]
