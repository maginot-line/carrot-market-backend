from rest_framework import exceptions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from categories.models import Category
from . import models, serializers

# Create your views here.
class Products(APIView):
    def get(self, request):
        all_products = models.Product.objects.all()
        serializer = serializers.ProductListSerializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = serializers.ProductDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise exceptions.ParseError("Category is required")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKind.COMMUNITY:
                        raise exceptions.ParseError("Community category is not allowed")
                except Category.DoesNotExist:
                    raise exceptions.NotFound("Category not found")
                product = serializer.save(user=request.user, category=category)
                serializer = serializers.ProductDetailSerializer(product)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": "You must be logged in to create a product."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Product.objects.get(pk=pk)
        except models.Product.DoesNotExist:
            raise exceptions.NotFound("Product does not exist")

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = serializers.ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)
        if not request.user.is_authenticated:
            return Response(
                {"error": "You must be logged in to update a product."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if product.user != request.user:
            return Response(
                {"error": "You can only update your own products."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        serializer = serializers.ProductDetailSerializer(
            product, data=request.data, partial=True
        )
        if serializer.is_valid():
            if request.data.get("category"):
                category_pk = request.data.get("category")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKind.COMMUNITY:
                        raise exceptions.ParseError("Community category is not allowed")
                except Category.DoesNotExist:
                    raise exceptions.NotFound("Category not found")
                updated_product = serializer.save(category=category)
            updated_product = serializer.save()
            return Response(
                serializers.ProductDetailSerializer(updated_product).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if not request.user.is_authenticated:
            return Response(
                {"error": "You must be logged in to delete a product."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if product.user != request.user:
            return Response(
                {"error": "You can only delete your own products."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
