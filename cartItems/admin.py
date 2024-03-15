from django.contrib import admin

from cartItems.models import CartItem


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    pass
