from django.contrib.auth.models import User
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import UserCreateSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def perform_create(self, serializer):
        queryset = User.objects.filter(username=serializer.data["username"])
        if queryset.exists():
            raise DjangoValidationError('You have already signed up')
        else:
            obj = User.objects.create(
                username=serializer.data["email"],
                email=serializer.data["email"],
                first_name=serializer.data["first_name"],
                last_name=serializer.data["last_name"]
            )
            obj.set_password(serializer.data["password"])
            obj.save()
