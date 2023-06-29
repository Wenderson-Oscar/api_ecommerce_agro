from .product_serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from ..models import Product


class ProductCreateListViewSets(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer