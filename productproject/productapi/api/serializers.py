from rest_framework import serializers
from productapi.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('id',
                'nome',
                'descricao',
                'quantidade',
                'preco')