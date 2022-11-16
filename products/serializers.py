from rest_framework import serializers
from categories.serializers import CategorySerializer
from users.serializers import TinyUserSerializer
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "category",
            "price",
            "description",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    category = CategorySerializer()

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
