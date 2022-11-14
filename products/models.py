from django.db import models
from common.models import CommonModel

# Create your models here.
class Product(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # image
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        "categories.Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    price = models.PositiveIntegerField()
    give_away = models.BooleanField(default=False)
    get_price_offer = models.BooleanField(default=False)
    description = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
