# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

from rest_framework import generics, mixins
from rest_framework import viewsets, authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from authcustom.serializers import *


class DefaultMixin(object):
    """ configuração default para api """
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )
    permission_classes = (permissions.AllowAny,)
    paginate_by = 10


@api_view(['GET'])
def user(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class UserListAuth(DefaultMixin, generics.ListAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # def perform_create(self, serializer):
    #     serializer.save()

    def perform_create(self, serializer):
        queryset = User.objects.filter(username=serializer.data["username"])
        if queryset.exists():
            raise ValidationError('You have already signed up')
        else:
            obj = User.objects.create(
                username=serializer.data["email"],
                email=serializer.data["email"],
                first_name=serializer.data["first_name"],
                last_name=serializer.data["last_name"]
            )
            obj.set_password(serializer.data["password"])
            obj.save()
