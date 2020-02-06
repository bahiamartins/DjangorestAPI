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
    authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication, authentication.TokenAuthentication)
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

class UserList(DefaultMixin, generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    #paginate_by = 10
    
    def perform_create(self, serializer):
        serializer.save()
