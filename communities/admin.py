from django.contrib import admin
from .models import Community, Answer, Wonder

# Register your models here.
@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "question",
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "community",
        "answer",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")


@admin.register(Wonder)
class WonderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "community",
        "wonder",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
