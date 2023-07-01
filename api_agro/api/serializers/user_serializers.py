from rest_framework import serializers
from ...models import User


class ReadUserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'profile', 'name', 'email', 'phone')


class CreateUserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'profile', 'name', 'email', 'phone', 'password']


