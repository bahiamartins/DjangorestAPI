from django.contrib.auth.models import User
from rest_framework.serializers import CharField, ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'is_active',
            'last_login'
        )


class UserCreateSerializer(ModelSerializer):
    password = CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
