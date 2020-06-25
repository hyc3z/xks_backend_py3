from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils.encoding import smart_text
from rest_framework.authtoken.serializers import AuthTokenSerializer
import base64
import sysadmin.models

class SystemAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = sysadmin.models.SystemAdmin
        fields = '__all__'
    
class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = sysadmin.models.Term
        fields = '__all__'

class LoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        try:
            username = sysadmin.models.SystemAdmin.objects.get(
                adminname=attrs['username'],
            ).user.username
        except sysadmin.models.SystemAdmin.DoesNotExist:
            username = get_random_string(
                length=8,
                allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789",
            )
        attrs['username'] = username
        p = attrs['password']
        attrs['password'] = smart_text(base64.decodebytes(bytes(p, 'utf-8')))
        return super().validate(attrs)