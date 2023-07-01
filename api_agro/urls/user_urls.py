from django.urls import path
from api_agro.api import UserListView, UserCreateView, GetUserView, UpdateUserView


urlpatterns = [
    path('', UserListView.as_view(), name='list_user'),
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('get_user/', GetUserView.as_view({'get': 'list'}), name='get_user'),
    path('update_user/<int:id>/', UpdateUserView.as_view(), name='update_user'),
]