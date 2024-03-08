from django.urls import path

from users.views import users_list


urlpatterns = [path("/", users_list)]
