from django.contrib import admin
from .models import Product

# Register your models here.
@admin.action(description="Set all price to zero")
def reset_prices(modeladmin, request, products):
    for product in products.all():
        product.price = 0
        product.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    list_display = (
        "user",
        "name",
        "category",
        "price",
        "give_away",
        "get_price_offer",
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
    )
    list_filter = ("category", "created_at", "updated_at")
    search_fields = ("name", "^price", "=user__username")
