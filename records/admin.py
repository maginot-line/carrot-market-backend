from django.contrib import admin
from .models import Record

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "product",
        "created_at",
        "updated_at",
    )
    list_filter = ("kind",)
