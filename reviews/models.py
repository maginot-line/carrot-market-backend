from django.db import models
from common.models import CommonModel

# Create your models here.
class Review(CommonModel):
    created_by_user = models.ForeignKey(
        "users.User", related_name="reviews_created_by_user", on_delete=models.CASCADE
    )
    created_for_user = models.ForeignKey(
        "users.User", related_name="reviews_created_for_user", on_delete=models.CASCADE
    )
    review = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{'⭐' * self.rating}"
