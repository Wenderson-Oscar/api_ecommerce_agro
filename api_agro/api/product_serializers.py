from rest_framework import serializers
from ..models import Product


class CreateProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'profile', 'description', 'value')


    def create(self, validated_data):
        user = self.context['request'].user
        product = Product.objects.create(user=user, **validated_data)
        return product


class ReadProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'