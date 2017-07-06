#!/path/to/python
# -*- coding: utf-8 -*-
#! /usr/bin/env python
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.

#用户信息
class User(models.Model):
    UserName  = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'账户名')
    UserNameCN= models.CharField(max_length=99,null=True,blank=True,verbose_name=u'中文名')
    Password  = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'密码')
    UserID    = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'员工编号')
    #用户类型用于用户鉴权
    UserType  = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'用户类型')
    #用户状态用于用户删除（有效性判断）
    UserState = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'用户状态')
    def __unicode__(self):
        return self.UserName

    class Meta:
        verbose_name = u'用户信息表'

class UserAdmin(admin.ModelAdmin):
    list_display  = ['UserName','UserNameCN','Password','UserID','UserType','UserState']
    list_editable = ['Password','UserNameCN','UserID','UserType','UserState']

#课程信息
class Plan(models.Model):
    PlanDigital = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'课程唯一标识')
    PlanNum     = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'首页课程编号')
    PlanStat    = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'是否激活')
    UpdateTime  = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'本次课程信息更新时间')
    Title1      = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'标题1')
    Title2      = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'标题2')
    Days        = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'课程培训天数')
    UnitsConcerned  = models.TextField(null=True,blank=True,verbose_name=u'各相关单位')
    TrainMainContent= models.TextField(null=True,blank=True,verbose_name=u'培训主要内容')
    WhenWhere       = models.TextField(null=True,blank=True,verbose_name=u'上课时间及地点')
    Joinner         = models.TextField(null=True,blank=True,verbose_name=u'参加对象')
    TrainInfo       = models.TextField(null=True,blank=True,verbose_name=u'师资、培训方式与目标')
    Certificate     = models.TextField(null=True,blank=True,verbose_name=u'颁发证书')
    Price           = models.TextField(null=True,blank=True,verbose_name=u'培训费用')
    Contact         = models.TextField(null=True,blank=True,verbose_name=u'联系人')
    ApplyWay        = models.TextField(null=True,blank=True,verbose_name=u'报名联系')
    Title_details   = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'详情页标题')
    #Plan_content    = models.TextField(null=True,blank=True,verbose_name=u'详情页正文')
    PDF_upload      = models.TextField(null=True,blank=True,verbose_name=u'PDF拥有者')
    PDF_exist       = models.CharField(max_length=5,default='0',verbose_name=u'是否有PDF')
    def __unicode__(self):
        return self.Title_details
    class Meta:
        verbose_name = u'培训班信息表'

class PlanAdmin(admin.ModelAdmin):
    list_display = ['PlanDigital','PlanNum','PlanStat','UpdateTime','Title1','Title2','Days','Title_details','PDF_upload','UnitsConcerned','TrainMainContent','WhenWhere','Joinner','TrainInfo','Certificate','Price','Contact','ApplyWay','PDF_exist']
    list_editable = ['PlanNum','PlanStat','UpdateTime','Title1','Title2','Days','Title_details','PDF_upload','UnitsConcerned','TrainMainContent','WhenWhere','Joinner','TrainInfo','Certificate','Price','Contact','ApplyWay','PDF_exist']

#PDF路径信息
class PDFPath(models.Model):
    PlanDigital = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'课程唯一标识')
    PlanNum     = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'课程编号')
    UserID      = models.CharField(max_length=99,null=True,blank=True,verbose_name=u'用户ID')
    PDF_path    = models.TextField(null=True,blank=True,verbose_name=u'PDF路径信息')
    def __unicode__(self):
        return self.PlanNum

    class Meta:
        verbose_name =u'PDF信息表'

class PDFPathAdmin(admin.ModelAdmin):
    list_display = ['PlanDigital','PlanNum','UserID','PDF_path']
    list_editable = ['PlanNum','UserID','PDF_path']

