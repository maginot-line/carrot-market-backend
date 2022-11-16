from rest_framework import exceptions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
class Products(APIView):
    def get(self, request):
        all_products = models.Product.objects.all()
        serializer = serializers.ProductListSerializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save(user=request.user)
            serializer = serializers.ProductDetailSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        pass

    def delete(self, request, pk):
        pass
