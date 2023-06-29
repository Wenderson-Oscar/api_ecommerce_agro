from .product_serializers import CreateProductSerializer, ReadProductSerializer
from rest_framework import viewsets, generics
from ..models import Product


class CreateProductView(generics.CreateAPIView):

    serializer_class = CreateProductSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return Product.objects.filter(user=self.get_object())


class ReadProductView(generics.ListAPIView):

    serializer_class = ReadProductSerializer
    queryset = Product.objects.all()


class GetProductView(viewsets.ModelViewSet):

    serializer_class = ReadProductSerializer

    def get_object(self):
        return self.request.user
    
    def get_queryset(self):
        return Product.objects.filter(user=self.get_object())
    

class DeleteProductView(generics.DestroyAPIView):

    serializer_class = ReadProductSerializer
    lookup_field = 'id'
    
    def get_object(self):
        return self.request.user
    
    def get_queryset(self):
        return Product.objects.filter(user=self.get_object())