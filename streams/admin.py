from django.contrib import admin
from .models import Stream

# Register your models here.
@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "price", "created_at", "updated_at")
    list_filter = (
        "user",
        "created_at",
        "updated_at",
    )
