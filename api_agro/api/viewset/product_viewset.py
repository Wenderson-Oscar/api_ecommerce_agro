from ..serializers.product_serializers import CreateProductSerializer, ReadProductSerializer
from rest_framework import generics
from ...models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class CreateProductView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CreateProductSerializer


class ReadProductView(generics.ListAPIView):

    serializer_class = ReadProductSerializer
    queryset = Product.objects.order_by('name')


class DeleteProductView(generics.RetrieveDestroyAPIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReadProductSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Product.objects.filter(user__id=self.request.user.id)
    

class UpdateProductView(generics.RetrieveUpdateAPIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReadProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Product.objects.filter(user__id=self.request.user.id)