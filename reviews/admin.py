from django.contrib import admin
from .models import Review

# Register your models here.
class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [("good", "Good"), ("great", "Great"), ("awesome", "Awesome")]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(review__contains=word)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "created_by_user",
        "created_for_user",
        "__str__",
        "created_at",
        "updated_at",
    )
    list_filter = (WordFilter, "created_by_user", "created_for_user", "rating")
