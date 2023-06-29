from rest_framework import viewsets, generics
from ..models import User
from .user_serializers import CreateUserSerializer, ReadUserSerializer


class UserCreateView(generics.CreateAPIView):

    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):

    serializer_class = ReadUserSerializer
    queryset = User.objects.all()


class GetUserView(viewsets.ModelViewSet):

    serializer_class = ReadUserSerializer

    def get_object(self):
        return self.request.user
    
    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

