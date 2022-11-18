from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=20, blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    avatar = models.FileField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, default="")

    def rating(self):
        count = self.reviews_created_for_user.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in self.reviews_created_for_user.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)

    def wishlists_count(self):
        count = self.wishlists.values("products").count()
        if count == 0:
            return 0
        else:
            return count
