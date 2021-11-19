from rest_framework import serializers
from userapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id',
            'login',
            'senha',
            'data_nascimento')