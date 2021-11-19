from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import serializers, status
 
from productapi.models import Product
from productapi.api.serializers import ProductSerializer
from rest_framework.decorators import api_view

@api_view(http_method_names=['GET'])
def product_list(request):
    products = Product.objects.all()
    serializers_product = ProductSerializer(products, many=True)
    return Response(serializers_product.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['POST'])
def product_create(request):

    if not request.data.get('nome') or not request.data.get('descricao') or\
        not request.data.get('quantidade') or not request.data.get('preco'):
        return Response({'error': 'todos os parametros devem ser preenchidos'}, status=status.HTTP_400_BAD_REQUEST)

    data = {
        'nome':request.data.get('nome'),
        'descricao':request.data.get('descricao'),
        'quantidade':request.data.get('quantidade'),
        'preco':request.data.get('preco'),
    }
    serialized_product = ProductSerializer(data=data)
    
    if serialized_product.is_valid():
        serialized_product.save()
        return Response(serialized_product.data, status=status.HTTP_201_CREATED)

    return Response(serialized_product.errors, status=status.HTTP_400_BAD_REQUEST)

def get_product_id(id):
    try:
        return Product.objects.get(id=id)
    except Product.DoesNotExist:
        return None

@api_view(http_method_names=['GET'])
def product_detail(request, id):
    product_instance = get_product_id(id)
    if not product_instance:
        return Response({"message":"Produto não encontrado"}, 
                        status=status.HTTP_400_BAD_REQUEST
                )
    serializer_product = ProductSerializer(product_instance)
    return Response(serializer_product.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['DELETE'])
def product_delete(request, id):
    product_instance = get_product_id(id)
    if not product_instance:
        return Response({"message":"Produto não encontrado"}, 
                        status=status.HTTP_400_BAD_REQUEST
                )

    product_instance.delete()
    
    return Response({"message":"Produto deletado com Sucesso!"},
                    status=status.HTTP_200_OK
    )

@api_view(http_method_names=["PUT"])
def product_change(request, id):
    product_instance = get_product_id(id)
    if not product_instance:
        return Response({"message":"Produto não encontrado"}, 
                        status=status.HTTP_400_BAD_REQUEST
                )

    
    if not request.data.get('nome') or not request.data.get('descricao') or\
        not request.data.get('quantidade') or not request.data.get('preco'):
        return Response({'error': 'todos os parametros devem ser preenchidos'}, status=status.HTTP_400_BAD_REQUEST)

    data = {
        'nome':request.data.get('nome'),
        'descricao':request.data.get('descricao'),
        'quantidade':request.data.get('quantidade'),
        'preco':request.data.get('preco'),
    }
    serialized_product = ProductSerializer( instance=product_instance, data=data, partial=True)
    
    if serialized_product.is_valid():
        serialized_product.save()
        return Response(serialized_product.data, status=status.HTTP_200_OK)

    return Response(serialized_product.errors, status=status.HTTP_400_BAD_REQUEST)