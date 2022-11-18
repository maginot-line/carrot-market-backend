from rest_framework import serializers
from products.serializers import ProductListSerializer
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ("pk", "products")
