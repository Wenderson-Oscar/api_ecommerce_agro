from rest_framework import viewsets, generics
from ...models import User
from ..serializers.user_serializers import CreateUserSerializer, ReadUserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response({'message': f'logado como {user.name if user.name else user.email }.'})
    
    
class UserCreateView(generics.CreateAPIView):

    permission_classes = [AllowAny] 
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReadUserSerializer(queryset, many=True)
        return Response(serializer.data)
        

class UserListView(generics.ListAPIView):

    serializer_class = ReadUserSerializer
    queryset = User.objects.all()


class GetUserView(viewsets.ModelViewSet):

    serializer_class = ReadUserSerializer
    
    def get_queryset(self):
        return  User.objects.filter(id=self.request.user.id)


class UpdateUserView(generics.RetrieveUpdateAPIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReadUserSerializer

    def get_queryset(self):
        return  User.objects.filter(id=self.request.user.id)