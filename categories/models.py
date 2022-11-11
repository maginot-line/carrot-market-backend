from django.db import models
from common.models import CommonModel

# Create your models here.
class Category(CommonModel):
    class CategoryKind(models.TextChoices):
        PRODUCT = "product", "Product"
        COMMUNITY = "community", "Community"

    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100, choices=CategoryKind.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
