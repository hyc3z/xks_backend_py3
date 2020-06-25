from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils.encoding import smart_text
from rest_framework.authtoken.serializers import AuthTokenSerializer
import base64
import teacher.models

class OfferCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher.models.OfferCourse
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher.models.Teacher
        fields = '__all__'

class LoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        try:
            username = teacher.models.Teacher.objects.get(
                tname=attrs['username'],
            ).user.username
        except teacher.models.Teacher.DoesNotExist:
            username = get_random_string(
                length=8,
                allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789",
            )
        attrs['username'] = username
        p = attrs['password']
        attrs['password'] = smart_text(base64.decodebytes(bytes(p, 'utf-8')))
        return super().validate(attrs)