from django.urls import path
from api_agro.api import ReadProductView, CreateProductView, DeleteProductView, UpdateProductView


urlpatterns = [
    path('list_product/', ReadProductView.as_view(), name='list_product'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('delete_product/<int:id>/', DeleteProductView.as_view(), name='delete_product'),
    path('update_product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
]
