from rest_framework import serializers
from ...models import Product


class CreateProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'profile', 'description', 'value')


    def create(self, validated_data):
        user_id = self.context['view'].kwargs['user_id']
        validated_data['user_id'] = user_id
        product = Product.objects.create(**validated_data)
        return product


class ReadProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    owner_name = serializers.CharField(source='user.name', read_only=True)
    owner_phone = serializers.CharField(source='user.phone', read_only=True)
    owner_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'