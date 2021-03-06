# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDFPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlanDigital', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u8bfe\u7a0b\u552f\u4e00\u6807\u8bc6')),
                ('PlanNum', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u8bfe\u7a0b\u7f16\u53f7')),
                ('UserID', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u7528\u6237ID')),
                ('PDF_path', models.TextField(blank=True, null=True, verbose_name='PDF\u8def\u5f84\u4fe1\u606f')),
            ],
            options={
                'verbose_name': 'PDF\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlanDigital', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u8bfe\u7a0b\u552f\u4e00\u6807\u8bc6')),
                ('PlanNum', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u9996\u9875\u8bfe\u7a0b\u7f16\u53f7')),
                ('PlanStat', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('UpdateTime', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u672c\u6b21\u8bfe\u7a0b\u4fe1\u606f\u66f4\u65b0\u65f6\u95f4')),
                ('Title1', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u6807\u98981')),
                ('Title2', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u6807\u98982')),
                ('Days', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bfe\u7a0b\u57f9\u8bad\u5929\u6570')),
                ('UnitsConcerned', models.TextField(blank=True, null=True, verbose_name='\u5404\u76f8\u5173\u5355\u4f4d')),
                ('TrainMainContent', models.TextField(blank=True, null=True, verbose_name='\u57f9\u8bad\u4e3b\u8981\u5185\u5bb9')),
                ('WhenWhere', models.TextField(blank=True, null=True, verbose_name='\u4e0a\u8bfe\u65f6\u95f4\u53ca\u5730\u70b9')),
                ('Joinner', models.TextField(blank=True, null=True, verbose_name='\u53c2\u52a0\u5bf9\u8c61')),
                ('TrainInfo', models.TextField(blank=True, null=True, verbose_name='\u5e08\u8d44\u3001\u57f9\u8bad\u65b9\u5f0f\u4e0e\u76ee\u6807')),
                ('Certificate', models.TextField(blank=True, null=True, verbose_name='\u9881\u53d1\u8bc1\u4e66')),
                ('Price', models.TextField(blank=True, null=True, verbose_name='\u57f9\u8bad\u8d39\u7528')),
                ('Contact', models.TextField(blank=True, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('ApplyWay', models.TextField(blank=True, null=True, verbose_name='\u62a5\u540d\u8054\u7cfb')),
                ('Title_details', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u8be6\u60c5\u9875\u6807\u9898')),
                ('PDF_upload', models.TextField(blank=True, null=True, verbose_name='PDF\u62e5\u6709\u8005')),
                ('PDF_exist', models.CharField(default='0', max_length=5, verbose_name='\u662f\u5426\u6709PDF')),
            ],
            options={
                'verbose_name': '\u57f9\u8bad\u73ed\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u8d26\u6237\u540d')),
                ('UserNameCN', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u4e2d\u6587\u540d')),
                ('Password', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u5bc6\u7801')),
                ('UserID', models.CharField(blank=True, max_length=99, null=True, verbose_name='\u5458\u5de5\u7f16\u53f7')),
                ('UserType', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u7528\u6237\u7c7b\u578b')),
                ('UserState', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u7528\u6237\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f\u8868',
            },
        ),
    ]
