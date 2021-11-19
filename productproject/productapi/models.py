from django.db import models

# Create your models here.
class Product(models.Model):
    nome = models.CharField(max_length=20, blank=False, default='')
    descricao = models.CharField(max_length=70,blank=False, default='')
    quantidade = models.IntegerField(blank=False,default=0)
    preco = models.FloatField(blank=False, default=0)

