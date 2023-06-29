"""
URL configuration for controller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_agro.api import (CreateProductView, 
                          GetProductView, ReadProductView, 
                          UserCreateView, GetUserView, 
                          UserListView, DeleteProductView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReadProductView.as_view(), name='list_product'),
    path('list_user/', UserListView.as_view(), name='list_user'),
    path('create/user/', UserCreateView.as_view(), name='user'),
    path('list_product/get_product/', GetProductView.as_view({'get': 'list'}), name='get_product'),
    path('list_product/create_product/', CreateProductView.as_view(), name='create_product'),
    path('user/get_user/', GetUserView.as_view({'get': 'list'}), name='get_user'),
    path('delete_product/<int:id>/', DeleteProductView.as_view(), name='delete_product'),
]
