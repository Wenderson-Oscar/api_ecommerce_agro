from ..serializers.product_serializers import CreateProductSerializer, ReadProductSerializer
from rest_framework import generics
from ...models import Product
from rest_framework.permissions import AllowAny



class CreateProductView(generics.CreateAPIView):

    permission_classes = []
    serializer_class = CreateProductSerializer
    queryset = Product.objects.all()


class ReadProductView(generics.ListAPIView):

    serializer_class = ReadProductSerializer
    queryset = Product.objects.select_related('user').order_by('name')


class ReadMyProductView(generics.ListAPIView):

    serializer_class = ReadProductSerializer

    def get_queryset(self):
        user_id = self.kwargs['id'] 
        return Product.objects.filter(user__id=user_id)


class DeleteProductView(generics.RetrieveDestroyAPIView):

    permission_classes = [AllowAny]
    serializer_class = ReadProductSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs['id'] 
        return Product.objects.filter(id=user_id)
    

class UpdateProductView(generics.RetrieveUpdateAPIView):

    serializer_class = ReadProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Product.objects.filter(user__id=self.request.user.id)