from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils.encoding import smart_text
from rest_framework.authtoken.serializers import AuthTokenSerializer
import base64
import student.models
import teacher.models
import sysadmin.models

class ChooseCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = student.models.ChooseCourse
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student.models.Student
        fields = '__all__'

class LoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        try:
            username = student.models.Student.objects.get(
                sname=attrs['username'],
            ).user.username
        except student.models.Student.DoesNotExist:
            username = get_random_string(
                length=8,
                allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789",
            )
        attrs['username'] = username
        p = attrs['password']
        attrs['password'] = smart_text(base64.decodebytes(bytes(p, 'utf-8')))
        return super().validate(attrs)

class GetOfferCoursesSerializer(serializers.ModelSerializer):
    class TeacherSerializer(serializers.ModelSerializer):
        class Meta:
            model = teacher.models.Teacher
            fields = ['tname','tid']
    
    class CourseSerializer(serializers.ModelSerializer):
        class Meta:
            model = sysadmin.models.Course
            fields = ['cid','cname','score']

    class TermSerializer(serializers.ModelSerializer):
        class Meta:
            model = sysadmin.models.Term
            fields = ['termname']

    class CampusSerializer(serializers.ModelSerializer):
        class Meta:
            model = sysadmin.models.Campus
            fields = ['xname']

    tid = TeacherSerializer(read_only=True)
    cid = CourseSerializer(read_only=True)
    termid=TermSerializer(read_only=True)
    xid=CampusSerializer(read_only=True)

    class Meta:
        model = teacher.models.OfferCourse
        fields = ['id','tid','cid','termid','maxnum','xid','time','place']

class ChooseCourseSerializer(serializers.Serializer):
    ocid=serializers.IntegerField()

class ChosenCoursesSerializer(serializers.ModelSerializer):
    ocid = GetOfferCoursesSerializer(read_only=True)

    class Meta:
        model = student.models.ChooseCourse
        fields = ['ocid']

class CourseScoreSerializer(serializers.ModelSerializer):
    class OCSerializer(serializers.ModelSerializer):
        class TeacherSerializer(serializers.ModelSerializer):
            class Meta:
                model = teacher.models.Teacher
                fields = ['tname','tid']
        
        class CourseSerializer(serializers.ModelSerializer):
            class Meta:
                model = sysadmin.models.Course
                fields = ['cid','cname','score']

        tid = TeacherSerializer(read_only=True)
        cid = CourseSerializer(read_only=True)

        class Meta:
            model = teacher.models.OfferCourse
            fields = ['id','tid','cid']

    ocid = OCSerializer(read_only=True)

    class Meta:
        model = student.models.ChooseCourse
        fields = ['ocid','pscore','kscore','zscore']

