from rest_framework import serializers
from categories.serializers import CategorySerializer
from users.serializers import TinyUserSerializer
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "is_owner",
            "name",
            "category",
            "price",
            "description",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
        )

    def get_is_owner(self, product):
        request = self.context["request"]
        return product.user == request.user


class ProductDetailSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "user",
            "is_owner",
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

    def get_is_owner(self, product):
        request = self.context["request"]
        return product.user == request.user
