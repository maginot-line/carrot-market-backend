from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
