from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, views, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action, permission_classes

import sysadmin.models
import sysadmin.serializers
import base64

class TermViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sysadmin.models.Term.objects.all()
    serializer_class = sysadmin.serializers.TermSerializer
    filter_fields = ['id']
    ordering_fields = '__all__'


class SystemAdminViewSet(viewsets.ModelViewSet):
    queryset = sysadmin.models.SystemAdmin.objects.all()
    serializer_class=sysadmin.serializers.SystemAdminSerializer

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def login(self, request, *args, **kwargs):
        info={}
        if request.data['adminid']=="" or request.data['password']=="":
            return Response('Serializer is invalid', 400)
        try:
            adminname = sysadmin.models.SystemAdmin.objects.get(
                adminid=request.data['adminid'],
            ).adminname
        except sysadmin.models.SystemAdmin.DoesNotExist:
            return Response('Serializer is invalid', 400)
        info["username"]=adminname
        info["password"]=request.data['password']
        serializer = sysadmin.serializers.LoginSerializer(
            data=info,
            context={'request': request}
        )
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
            })
        else:
            return Response('Serializer is invalid', 400)