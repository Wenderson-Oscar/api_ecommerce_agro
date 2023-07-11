from django.db import models
from .user import User

class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ImageField(verbose_name='Foto', default='product/auto.png' ,upload_to='product/', blank=True, null=True)
    name = models.CharField(verbose_name='Nome do Produto', max_length=100)
    description = models.TextField(verbose_name='Descrição do Produto')
    value = models.FloatField(verbose_name='Valor')


    def __str__(self):
        return self.name