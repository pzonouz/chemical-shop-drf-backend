from django.urls import path, re_path

from auth.views import CustomProviderAuthView, LoginView, LogoutView


urlpatterns = [
    path("login", LoginView.as_view()),
    re_path(
        r"^o/(?P<provider>\S+)/$",
        CustomProviderAuthView.as_view(),
        name="provider-auth",
    ),
    path("logout", LogoutView.as_view()),
]
