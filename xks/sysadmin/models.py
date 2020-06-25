from django.db import models
from django.contrib.auth.models import User

class SystemAdmin(models.Model):
    '''
    [管理员表]
    adminid:管理员号
    adminname:管理员姓名
    user:Django自带user
    '''
    adminid=models.CharField(max_length=100,blank=False,unique=True,primary_key=True)  
    adminname=models.CharField(max_length=100,blank=False)
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        blank=False
    )

class Campus(models.Model):
    '''
    [校园表]
    xid:校区号
    xname:校区地点
    '''
    xid=models.CharField(max_length=100,blank=False,unique=True,primary_key=True)  
    xname=models.CharField(max_length=100,blank=False)

class Term(models.Model):
    '''
    [学期表]
    termname:学期名
    '''
    termname=models.CharField(max_length=100,blank=False)  

class School(models.Model):
    '''
    [院系表]
    schoolid:院系id
    schoolname:院系名
    '''
    schoolid=models.CharField(max_length=100,blank=False,unique=True,primary_key=True)  
    schoolname=models.CharField(max_length=100,blank=False)

class Course(models.Model):
    '''
    [课程组表]
    cid:课程号
    cname:课程名
    score:学分
    '''
    cid=models.CharField(max_length=100,blank=False,unique=True,primary_key=True)  
    cname=models.CharField(max_length=100,blank=False)
    score=models.IntegerField(blank=False)
    