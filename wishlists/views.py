from django.db import transaction
from rest_framework import exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Product
from . import models, serializers

# Create your views here.
class Wishlists(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, user):
        try:
            return models.Wishlist.objects.get(user=user)
        except models.Wishlist.DoesNotExist:
            raise exceptions.NotFound("Wishlist not found")

    def get(self, request):
        wishlist = self.get_object(request.user)
        serializer = serializers.WishlistSerializer(
            wishlist, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        user = models.Wishlist.objects.filter(user=request.user)
        if user:
            raise exceptions.ParseError("You already have a wishlist")
        serializer = serializers.WishlistSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    wishlist = serializer.save(user=request.user)
                    products = request.data.get("products")
                    for product_pk in products:
                        product = Product.objects.get(pk=product_pk)
                        if not product_pk:
                            raise exceptions.ParseError("Product is required")
                        wishlist.products.add(product)
                    serializer = serializers.WishlistSerializer(
                        wishlist, context={"request": request}
                    )
                    return Response(serializer.data)
            except Exception:
                raise exceptions.ParseError("Product is required")
        else:
            return Response(serializer.errors)

    
class WishlistToggle(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, user):
        try:
            return models.Wishlist.objects.get(user=user)
        except models.Wishlist.DoesNotExist:
            raise exceptions.NotFound("Wishlist not found")

    def get_product(self, product_pk):
        try:
            return Product.objects.get(pk=product_pk)
        except Product.DoesNotExist:
            raise exceptions.NotFound("Product not found")

    def put(self, request, product_pk):
        wishlist = self.get_object(request.user)
        product = self.get_product(product_pk)
        if product:
            if wishlist.products.filter(pk=product.pk).exists():
                wishlist.products.remove(product)
            else:
                wishlist.products.add(product)
            serializer = serializers.WishlistSerializer(wishlist, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
