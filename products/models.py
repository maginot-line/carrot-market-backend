from django.db import models

# Create your models here.
class Product(models.Model):
    # image
    title = models.CharField(max_length=100)
    # category
    price = models.PositiveIntegerField()
    give_away = models.BooleanField(default=False)
    get_price_offer = models.BooleanField(default=False)
    description = models.TextField()
    latitude_to_trade = models.CharField(max_length=100)
    longitude_to_trade = models.CharField(max_length=100)
