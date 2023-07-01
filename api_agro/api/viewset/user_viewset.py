from rest_framework import viewsets, generics
from ...models import User
from ..serializers.user_serializers import CreateUserSerializer, ReadUserSerializer


class UserCreateView(generics.CreateAPIView):

    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):

    serializer_class = ReadUserSerializer
    queryset = User.objects.all()


class GetUserView(viewsets.ModelViewSet):

    serializer_class = ReadUserSerializer
    queryset = User.objects.all()


class UpdateUserView(generics.UpdateAPIView):

    serializer_class = ReadUserSerializer
    queryset = User.objects.all()