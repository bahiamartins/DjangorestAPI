from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserUpdateSerializer
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        # Muda o serializer dependendo da ação.
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == 'update':
            return UserUpdateSerializer
        return UserSerializer

    def perform_create(self, serializer):
        # Método para criar usuário.
        queryset = User.objects.filter(
            Q(username=serializer.data["email"]) |
            Q(email=serializer.data["email"])
        )
        if queryset.exists():
            raise DRFValidationError('E-mail já existe.')
        else:
            # username = email
            obj = User.objects.create(
                username=serializer.data["email"],
                email=serializer.data["email"],
                first_name=serializer.data["first_name"],
                last_name=serializer.data["last_name"]
            )
            obj.set_password(serializer.data["password"])
            obj.save()

    def retrieve(self, request, pk=None):
        # Método para ver os detalhes de um usuário.
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise DRFValidationError('Usuário não encontrado.')

        if request.user and request.user.is_authenticated:
            serializer = UserSerializer(user)
        else:
            raise DRFValidationError('Você não tem acesso a este usuário.')
        return Response(serializer.data)

    def perform_update(self, serializer):
        # Método para editar um usuário.
        instance = self.get_object()
        data = self.request.data
        request_user = self.request.user
        pk = instance.id

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise DRFValidationError('Usuário não encontrado.')

        if request_user and request_user.is_authenticated:
            if request_user == user:
                email = data["email"]
                if user.email == email:
                    raise DRFValidationError('Email igual ao já cadastrado.')
                elif User.objects.filter(email=email).exists():
                    raise DRFValidationError('Já existe um outro usuário com este email.')
            else:
                raise DRFValidationError('Você não tem permissão para esta operação.')
        return super(UserViewSet, self).perform_update(serializer)
