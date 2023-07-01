from ..serializers.product_serializers import CreateProductSerializer, ReadProductSerializer
from rest_framework import viewsets, generics
from ...models import Product


class CreateProductView(generics.CreateAPIView):

    serializer_class = CreateProductSerializer


class ReadProductView(generics.ListAPIView):

    serializer_class = ReadProductSerializer
    queryset = Product.objects.order_by('name')


class DeleteProductView(generics.DestroyAPIView):

    serializer_class = ReadProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    

class UpdateProductView(generics.UpdateAPIView):

    serializer_class = ReadProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'