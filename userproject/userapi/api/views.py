from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from userapi.models import User
from .serializers import UserSerializer

from userapi.tools.functions import gera_senha

class UserApiView(APIView):

    #return all users
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        print('teste ok')

        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK) 
    
    #create user..
    def post(self, request, *args, **kwargs):
        if not request.data.get('login') or not request.data.get('data_nascimento'):
            return Response({'error': 'login e data_nascimento devem ser preenchidos'}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'login': request.data.get('login'),
            'data_nascimento': request.data.get('data_nascimento')
        }

        if not request.data.get('senha'):
            data['senha'] = gera_senha(12)
        elif len(request.data.get('senha')) != 12:
            return Response({'error':'a senha deve ter 12 caracteres'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            data['senha'] = request.data.get('senha')

        serialized_data = UserSerializer(data=data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsView(APIView):
    
    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    #retorna detalhes de apenas um usuário...
    def get(self, request, user_id, *args, **kwargs):

        user_instance = self.get_object(user_id)

        if not user_instance:
            return Response(
                {"message":"Usuário não encontrado"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serialized_user = UserSerializer(user_instance)

        return Response(serialized_user.data, status=status.HTTP_200_OK)

    #altera usuário...
    def put(self, request,user_id,*args, **kwargs):

        user_instance = self.get_object(user_id)

        if not user_instance:
            return Response(
                {"message":"Usuário não encontrado"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not request.data.get('login') or not request.data.get('data_nascimento'):
            return Response({'error': 'login e data_nascimento devem ser preenchidos'}, status=status.HTTP_400_BAD_REQUEST)


        data = {
            'login': request.data.get('login'),
            'data_nascimento': request.data.get('data_nascimento')
        }

        if not request.data.get('senha'):
            data['senha'] = gera_senha(12)
        elif len(request.data.get('senha')) != 12:
            return Response({'error':'a senha deve ter 12 caracteres'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            data['senha'] = request.data.get('senha')

        serialized_data = UserSerializer(instance= user_instance, data=data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_200_OK)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    #deleta usuário pelo id...
    def delete(self, request,user_id,*args, **kwargs):

        user_instance = self.get_object(user_id)

        if not user_instance:
            return Response(
                {"message":"Usuário não encontrado"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_instance.delete()

        return Response({"message": "Usuário deletado com Sucesso!"},
                        status=status.HTTP_200_OK
                )