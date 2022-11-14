from django.db import models
from common.models import CommonModel

# Create your models here.
class Record(CommonModel):
    class KindChoices(models.TextChoices):
        FAV = "fav", "Favorite"
        PURCHASE = "purchase", "Purchase"
        SALE = "sale", "Sale"

    kind = models.CharField(max_length=20, choices=KindChoices.choices)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="records"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="records"
    )
