from .user_serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from ..models import User


class UserCreateListViewSets(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
