from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, views, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action, permission_classes

import teacher.models
import teacher.serializers
import base64

class OfferCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = teacher.models.OfferCourse.objects.all()
    serializer_class = teacher.serializers.OfferCourseSerializer
    filter_fields = ['cid']
    ordering_fields = '__all__'


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = teacher.models.Teacher.objects.all()
    serializer_class=teacher.serializers.TeacherSerializer

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def login(self, request, *args, **kwargs):
        info={}
        if request.data['tid']=="" or request.data['password']=="":
            return Response('Serializer is invalid', 400)
        try:
            tname = teacher.models.Teacher.objects.get(
                tid=request.data['tid'],
            ).tname
        except teacher.models.Teacher.DoesNotExist:
            return Response('Serializer is invalid', 400)
        info["username"]=tname
        info["password"]=request.data['password']
        serializer = teacher.serializers.LoginSerializer(
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