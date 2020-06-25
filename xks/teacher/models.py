from django.db import models
from django.contrib.auth.models import User
import sysadmin.models

class Teacher(models.Model):
    '''
    [教师表]
    tid:学号
    tname:姓名
    user:Django自带user
    schoolid:学院号
    '''
    tid=models.CharField(max_length=100,blank=False,unique=True,primary_key=True)  
    tname=models.CharField(max_length=100,blank=False)  
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        blank=False
    )
    schoolid=models.ForeignKey(
        to=sysadmin.models.School,
        on_delete=models.CASCADE,
        related_name='teacher',
        to_field="schoolid",
        blank=False
    )

class OfferCourse(models.Model):
    '''
    [开课表]
    tid:教师号
    cid:课程号
    termid:学期
    maxnum:最大人数
    xid:校区号
    time:上课时间
    place:上课地点
    '''
    tid = models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        related_name='offer_course',
        to_field="tid",
        blank=False
    )
    cid = models.ForeignKey(
        to=sysadmin.models.Course,
        on_delete=models.CASCADE,
        related_name='offer_course',
        to_field="cid",
        blank=False
    )
    termid= models.ForeignKey(
        to=sysadmin.models.Term,
        on_delete=models.CASCADE,
        related_name='offer_course',
        to_field="id",
        blank=False
    )
    maxnum=models.IntegerField(default=0) 
    xid = models.ForeignKey(
        to=sysadmin.models.Campus,
        on_delete=models.CASCADE,
        related_name='offer_course',
        to_field="xid",
        blank=False
    )
    time=models.CharField(max_length=100)
    place=models.CharField(max_length=100)  
    status=models.IntegerField(default=0) #0:未开始 1:进行中 2:课程结束



