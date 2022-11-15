from rest_framework import serializers
from categories.serializers import CategorySerializer
from users.serializers import TinyUserSerializer
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = TinyUserSerializer()

    class Meta:
        model = Product
        fields = (
            "user",
            "name",
            "category",
            "price",
            "give_away",
            "get_price_offer",
            "description",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
        )
