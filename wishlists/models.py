from django.db import models
from common.models import CommonModel

# Create your models here.
class Wishlist(CommonModel):
    user = models.ForeignKey(
        "users.User", related_name="wishlists", on_delete=models.CASCADE
    )
    products = models.ManyToManyField("products.Product", related_name="wishlists")
