from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "created_by_user",
        "created_for_user",
        "__str__",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_by_user", "created_for_user", "rating")
