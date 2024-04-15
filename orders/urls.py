from django.urls import path

from orders.views import orders_statuses

urlpatterns = [path("", orders_statuses)]
