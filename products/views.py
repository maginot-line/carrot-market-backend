from rest_framework import exceptions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductListSerializer

# Create your views here.
class Products(APIView):
    def get(self, request):
        all_products = Product.objects.all()
        serializer = ProductListSerializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass
