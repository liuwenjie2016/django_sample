#!/path/to/python
# -*- coding: utf-8 -*-
#! /usr/bin/env python
#
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import User,Plan,PDFPath
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import CharField,Value as V
from django.db.models.functions import Concat
import ConfigParser
import hashlib
import json
import sys
import time
reload(sys)
sys.setdefaultencoding("utf8")
# Create your views here.

def index(request):
    plan = Plan.objects.filter(PlanStat='yes')
    p0 = {}
    p1 = {}
    p2 = {}
    p3 = {}
    p4 = {}
    for i in plan:
        plannum = i.PlanNum
        title1 = i.Title1
        title2 = i.Title2
        days = i.Days
        if plannum == '1':
            p0['t1'] = title1
            p0['t2'] = title2
            p0['days'] = days

        if plannum == '2':
            p1['t1'] = title1
            p1['t2'] = title2
            p1['days'] = days

        if plannum == '3':
            p2['t1'] = title1
            p2['t2'] = title2
            p2['days'] = days

        if plannum == '4':
            p3['t1'] = title1
            p3['t2'] = title2
            p3['days'] = days

        if plannum == '5':
            p4['t1'] = title1
            p4['t2'] = title2
            p4['days'] = days
    user_id = request.GET.get('id')
    user_obj = User.objects.filter(UserID=user_id)
    if user_obj.exists():
        user_info = user_obj[0]
        user_name = user_info.UserNameCN
        return render_to_response('index.html',locals())
    else:
        return render_to_response('index.html',locals())

#历史课程详情
def plan_query_details(request,digital_id):
    planinfo = Plan.objects.filter(PlanDigital=digital_id)
    if planinfo.exists():
        plan_info = planinfo[0]
        plan = {}
        plan['title_details'] = plan_info.Title_details
        #plan['plan_content'] = plan_info.Plan_content
        plan['num']                 = plan_info.PlanNum
        plan['digital']             = digital_id
        plan['UnitsConcerned']      = plan_info.UnitsConcerned
        plan['TrainMainContent']    = plan_info.TrainMainContent
        plan['WhenWhere']           = plan_info.WhenWhere
        plan['Joinner']             = plan_info.Joinner
        plan['TrainInfo']           = plan_info.TrainInfo
        plan['Certificate']         = plan_info.Certificate
        plan['Price']               = plan_info.Price
        plan['ApplyWay']            = plan_info.ApplyWay
        plan['t1']                  = plan_info.Title1
        plan['t2']                  = plan_info.Title2
        plan['days']                = plan_info.Days
        plan['sign']                = '1'
    else:
        msg = '0001'
        return HttpResponse(msg)

    return render_to_response("edit.html",locals())

#课程详情页方法
def details(request,DetailsId):
    planinfo = Plan.objects.filter(PlanNum=DetailsId,PlanStat='yes')
    if planinfo.exists():
        plan_info = planinfo[0]
        plan = {}
        plan['title_details'] = plan_info.Title_details
        #plan['plan_content'] = plan_info.Plan_content
        plan['num'] = DetailsId
        plan['digital']             = plan_info.PlanDigital
        plan['UnitsConcerned']      = plan_info.UnitsConcerned
        plan['TrainMainContent']    = plan_info.TrainMainContent
        plan['WhenWhere']           = plan_info.WhenWhere
        plan['Joinner']             = plan_info.Joinner
        plan['TrainInfo']           = plan_info.TrainInfo
        plan['Certificate']         = plan_info.Certificate
        plan['Price']               = plan_info.Price
        plan['Contact']             = plan_info.Contact
        plan['ApplyWay']            = plan_info.ApplyWay
       # plan['pdf_exist']           = plan_info.
    else:
        msg = '0001'
        return HttpResponse(msg)

    return render_to_response("details1.html",locals())


#plan_details是用来渲染创建课程时对应课程ID的课程信息的方法
def plan_details(request,DetailsId):
    planinfo = Plan.objects.filter(PlanNum=DetailsId,PlanStat='yes')
    plan = {}
    plan['num'] = DetailsId
    if planinfo.exists():
        plan_info                   = planinfo[0]
        plan['t1']                  = plan_info.Title1
        plan['t2']                  = plan_info.Title2
        plan['days']                = plan_info.Days
        plan['title_details']       = plan_info.Title_details
        plan['digital']             = plan_info.PlanDigital
        plan['UnitsConcerned']      = plan_info.UnitsConcerned
        plan['TrainMainContent']    = plan_info.TrainMainContent
        plan['WhenWhere']           = plan_info.WhenWhere
        plan['Joinner']             = plan_info.Joinner
        plan['TrainInfo']           = plan_info.TrainInfo
        plan['Certificate']         = plan_info.Certificate
        plan['Price']               = plan_info.Price
        plan['Contact']             = plan_info.Contact
        plan['ApplyWay']            = plan_info.ApplyWay
        plan['sign']                = '0'
	
#	user_all		    = User.objects.all()
#	userlist 	            = []
#	for i in user_all:
#		userlist.append(i.UserName)
#	pdf_uploader		    = str(plan_info.PDF_upload)
#	user_pdf= {}
#	for i in userlist:
#		if i in pdf_uploader:
#			user_pdf[i] = {i:'1'}
#		else :
#			user_pdf[i] = {i:'0'}

    else:
        return render_to_response('edit.html',locals())

    return render_to_response("edit.html",locals())

##查看PDF
@xframe_options_exempt
@csrf_exempt
def pdf_path(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')
        digital = request.POST.get('digital','')
        PlanNum = request.POST.get('plan_num','')
        plan_obj = Plan.objects.filter(PlanNum=PlanNum,PlanStat='yes')
        if plan_obj.exists():
            digital = plan_obj[0].PlanDigital

            pdf_obj = PDFPath.objects.filter(PlanDigital=digital,UserID=user_id)
            if pdf_obj.exists():
                pdf_info = pdf_obj[0]
            #pdf_path = pdf_info.PDF_path.replace('/home/huitraining/HuiTraining/','')
                msg = pdf_info.PDF_path.replace('/www/huitraining/static/pdf/','')
                print msg.decode('utf-8')
            #msg = msg[0]
                print type(msg)
            #msg = json.dumps(pdf_path)
            #msg=msg[3:-2]
            #print msg
            #msg = msg.replace('\\','')
            #print msg
                return HttpResponse(msg)
            else:
                msg = '0'
                return HttpResponse(msg)
        else:
            msg = '0'
            return HttpResponse(msg)
    else:
        msg = '0001'
        return HttpResponse(msg)

@xframe_options_exempt
@csrf_exempt
def account_login(request):
    if request.method == 'POST':
        UserName = request.POST.get('UserName','')
        Password = request.POST.get('Password','')
        try:
            UserInfo = User.objects.filter(UserName=UserName)[0]
            UserPassword = UserInfo.Password
        except:
            access = "False"
            return HttpResponse(access)

        if Password == UserPassword:
            access= str(UserInfo.UserID)
            return HttpResponse(access)
        elif Password == hashlib.md5(UserPassword).hexdigest():
            UserInfo.Password = hashlib.md5(UserPassword).hexdigest()
            UserInfo.save()
            access= str(UserInfo.UserID)
            return HttpResponse(access)
        else:
            access = "False"
            return HttpResponse(access)
    else:
        return render_to_response('login.html',locals())

#查询课程
#@xframe_options_exempt
@csrf_exempt
def plan_query(request):
    if request.method == 'POST':
        plan_digital = request.POST.get("plan_digital")
        plan_obj = Plan.objects.filter(PlanDigital=plan_digital)
        if plan_obj.exists():
            plan_info = {}
            plan_info['PlanDigital'] = plan_obj.PlanDigital
            plan_info['PlanNum'] = plan_obj.PlanNum
            plan_info['PlanStat'] = plan_obj.PlanStat
            plan_info['UpdateTime'] = plan_obj.UpdateTime
            plan_info['Title1'] = plan_obj.Title1
            plan_info['Title2'] = plan_obj.Title2
            plan_info['Days'] = plan_obj.Days
            plan_info['UnitsConcerned'] = plan_obj.UnitsConcerned
            plan_info['TrainMainContent'] = plan_obj.TrainMainContent
            plan_info['WhenWhere'] = plan_obj.WhenWhere
            plan_info['Joinner'] = plan_obj.Joinner
            plan_info['TrainInfo'] = plan_obj.TrainInfo
            plan_info['Certificate'] = plan_obj.Certificate
            plan_info['Price'] = plan_obj.Price
            plan_info['ApplyWay'] = plan_obj.ApplyWay
            plan_info['Title_details'] = plan_obj.Title_details
            plan_info['PDF_upload'] = plan_obj.PDF_upload
            plan_info1 = json.dumps(plan_info)
            return HttpResponse(plan_info1)
    else:
        plans = Plan.objects.all()
        plan_list = []
        for i in plans:
            plan_info = {}
            plan_info['PlanDigital'] = i.PlanDigital
            plan_info['PlanNum'] = i.PlanNum
            plan_info['PlanStat'] = i.PlanStat
            plan_info['UpdateTime'] = i.UpdateTime
            plan_info['Title1'] = i.Title1
            plan_info['Title2'] = i.Title2
            plan_info['Days'] = i.Days
            plan_info['UnitsConcerned'] = i.UnitsConcerned
            plan_info['TrainMainContent'] = i.TrainMainContent
            plan_info['WhenWhere'] = i.WhenWhere
            plan_info['Joinner'] = i.Joinner
            plan_info['TrainInfo'] = i.TrainInfo
            plan_info['Certificate'] = i.Certificate
            plan_info['Price'] = i.Price
            plan_info['ApplyWay'] = i.ApplyWay
            plan_info['Title_details'] = i.Title_details
            plan_info['PDF_upload'] = i.PDF_upload
            plan_list.append(plan_info.copy())
        return render_to_response('query.html',locals())


#查询课程
@xframe_options_exempt
@csrf_exempt
def plan_query1111111111(request):#改用模板渲染了所以用get请求 重新写一个 T.T|||
    if request.method == 'POST':
        search_type = request.POST.get("search_type")
        keyword = request.POST.get("keyword")
        if search_type == 'all':      #如果search_type的值为all，则导出所有课程信息
            plans = Plan.objects.all()
        elif search_type == 'title':  #如果search_type的值为title 则用关键字keyword对title进行查找相关的课程信息
            plans = Plan.objects.filter(Title_details__contains=keyword)
        elif search_type == 'place':
            plans = Plan.objects.filter(WhenWhere__contains=keyword)
        elif search_type == 'UpdateTime':
            plans = Plan.objects.filter(UpdateTime__contains=keyword)
        elif search_type == 'days':
            plans = Plan.objects.filter(Days__contains=keyword)

        if plans.exists():
            plan_list = []
            for i in plans:
                plan_info = {}
                plan_info['PlanDigital'] = i.PlanDigital
                plan_info['PlanNum'] = i.PlanNum
                plan_info['PlanStat'] = i.PlanStat
                plan_info['UpdateTime'] = i.UpdateTime
                plan_info['Title1'] = i.Title1
                plan_info['Title2'] = i.Title2
                plan_info['Days'] = i.Days
                plan_info['UnitsConcerned'] = i.UnitsConcerned
                plan_info['TrainMainContent'] = i.TrainMainContent
                plan_info['WhenWhere'] = i.WhenWhere
                plan_info['Joinner'] = i.Joinner
                plan_info['TrainInfo'] = i.TrainInfo
                plan_info['Certificate'] = i.Certificate
                plan_info['Price'] = i.Price
                plan_info['ApplyWay'] = i.ApplyWay
                plan_info['Contact'] = i.Contact
                plan_info['Title_details'] = i.Title_details
                plan_info['PDF_upload'] = i.PDF_upload
                plan_list.append(plan_info.copy())
            plan_info_list = json.dumps(plan_list)
            return HttpResponse(plan_info_list)
        else:
            msg = '1000' #表示没有查询到相关课程信息
            return HttpResponse(msg)
        msg = 'test'
        return HttpResponse(msg) #表示用get方法不对，这个视图函数只接受post请求
    else:
        msg = '0001'
        return HttpResponse(msg)

#创建课程
#@xframe_options_exempt
@csrf_exempt
def edit_ini(request):
    if request.method == 'POST':
        plan_digital        = request.POST.get('digital','')
        UnitsConcerned      = request.POST.get('UnitsConcerned','')
        plan_num            = request.POST.get('plan_num','')
        t1                  = request.POST.get('t1','')
        t2                  = request.POST.get('t2','')
        days                = request.POST.get('days','')
        title_details       = request.POST.get('title_details','')
        TrainMainContent    = request.POST.get('TrainMainContent','')
        WhenWhere           = request.POST.get('WhenWhere','')
        Joinner             = request.POST.get('Joinner','')
        TrainInfo           = request.POST.get('TrainInfo','')
        Certificate         = request.POST.get('Certificate','')
        Price               = request.POST.get('Price','')
        Contact             = request.POST.get('Contact','')
        ApplyWay            = request.POST.get('ApplyWay','')
        PlanDigital = str(time.time()).replace('.','')
        today = time.strftime('%Y%m%d',time.localtime())
        if plan_num != '' and t1 != '' and t2 != '' and days != '' and title_details != '':
            plan = Plan.objects.filter(PlanNum=plan_num,PlanStat='yes')
            if plan.exists():
                plan.update(PlanStat = 'no')
                #plan[0].save()
                #plan[0].refresh_from_db()
		#plan[0].save()
                new_plan = Plan(PlanDigital=PlanDigital,PlanNum=plan_num,PlanStat='yes',UpdateTime=today,Title1=t1,Title2=t2,Days=days,
                Title_details=title_details,TrainMainContent=TrainMainContent,UnitsConcerned=UnitsConcerned,WhenWhere=WhenWhere,
                Joinner=Joinner,TrainInfo=TrainInfo,Certificate=Certificate,Price=Price,ApplyWay=ApplyWay,Contact=Contact)
                new_plan.save()
                new_plan.refresh_from_db()
                msg = '0000'
                return HttpResponse(msg)
            else:
                new_plan = Plan(PlanDigital=PlanDigital,PlanNum=plan_num,PlanStat='yes',UpdateTime=today,Title1=t1,Title2=t2,Days=days,
                Title_details=title_details,TrainMainContent=TrainMainContent,UnitsConcerned=UnitsConcerned,WhenWhere=WhenWhere,
                Joinner=Joinner,TrainInfo=TrainInfo,Certificate=Certificate,Price=Price,ApplyWay=ApplyWay,Contact=Contact)
                new_plan.save()
                new_plan.refresh_from_db()
                msg = '0000'
                return HttpResponse(msg)

        else:
                msg = '0001'
                return HttpResponse(msg)


    else:
        return render_to_response('edit.html',locals())

#
##上传PDF
#@xframe_options_exempt
@csrf_exempt
def pdf_upload(request):
    if request.POST.get('picurllist',''):
        pdfurl = str(request.POST.get('picurllist'))
#	pdfurl = eval(pdfurl)
	if pdfurl!=[]:
		pdfurl = str(pdfurl).replace(' ','')
		print pdfurl
#print type(pdfurl)
#print pdfurl
#pdfurl = pdfurl.replace('\\','')
		plan_num = request.POST.get('plan_num','')
		user_id = request.POST.get('name_id','')
		plan_obj = Plan.objects.filter(PlanNum=plan_num,PlanStat='yes')
		if plan_obj.exists():
			plan_digital = plan_obj[0].PlanDigital
			oldpath = PDFPath.objects.filter(PlanDigital=plan_digital,UserID=user_id)
		else:
			msg = '0011'
			return HttpResponse(msg)
		if oldpath.exists():
	#oldpath.update(PDF_path=pdfurl,PlanDigital=plan_digital)
	#oldpath[0].refresh_from_db()
			oldpath.update(PDF_path=pdfurl)
	#oldpath[0].save()
			oldpath[0].refresh_from_db()
	#oldpath.update(PDF_path=Concat('PDF_path',V(','+pdfurl)))
	#oldpath[0].refresh_from_db()
		else:
			newpath = PDFPath(PlanNum=plan_num,PDF_path=str(pdfurl),UserID=str(user_id),PlanDigital=plan_digital)
			newpath.save()
    #如果路径保存成功。则在课程信息中的已上传PDF者字段中加入该用户ID下的用户名
		user_obj = User.objects.filter(UserID=user_id)[0]
		user_name = user_obj.UserName
		plan_obj.update(PDF_upload=Concat('PDF_upload',V(','+user_name)))
		plan_obj[0].refresh_from_db()
		msg = '0000'
		return HttpResponse(msg)
	else:
		msg = '1111'
		return HttpResponse(msg)
		
            #msg = '0011'
            #return HttpResponse(msg)

    elif request.method == 'POST':
        pdf_file = request.FILES['file']
        #print pdf_file
	#print type(pdf_file)
        #print '1111111111111111111111'
        data = pdf_file.read()
        static_path = '/www/huitraining/static/pdf/'
        #up_time	= str(time.time()).replace('.','')
        pdf_path =str(static_path)+str(pdf_file).replace(' ','')
        with open(pdf_path,'w') as f:
            f.write(data)
            return HttpResponse(pdf_path)
    else :
        msg = '0001'
        return HttpResponse(msg)
    return render_to_response('edit.html',locals())


#点击【上传PDF】的时候传给前端用户列表，按照UserType及UserState筛选
@xframe_options_exempt
@csrf_exempt
def user_query(request):
    if request.POST.get('user_name',''):
        user_id = request.POST.get('user_name','')
        userinfo = User.objects.filter(UserID=user_id)
        if userinfo.exists():
            username = userinfo[0].UserNameCN
            username_json = json.dumps(username)
            return HttpResponse(username_json)
        else:
            msg = '0001'
            return HttpResponse(msg)

    if request.POST.get('user_query',''):
	plan_id =  request.POST.get('class_id','')
        id_list = []
        name_list = []
        userinfo = User.objects.filter(UserType='2',UserState='1')
        for i in userinfo:
            id_list.append(i.UserID)
            name_list.append(i.UserName)
	planinfo = Plan.objects.filter(PlanNum=plan_id,PlanStat='yes')
	if planinfo.exists():
		pdf_uploader                = str(planinfo[0].PDF_upload)
	
        user_info = []
        for (a,b) in zip(name_list,id_list):
            z = {}
            z['user_name'] = a
            z['user_id'] = b
	    if a in pdf_uploader:
	    	z['pdf_update'] = '1'
	    else:
		z['pdf_update'] = '0'
            user_info.append(z.copy())

        user_info1 = json.dumps(user_info)
        return HttpResponse(user_info1)
    else:
        msg = '0011'
        return HttpResponse(msg)

#增加用户
@xframe_options_exempt
@csrf_exempt
def user_manage(request):

#用户删除功能，更新功能，查询功能提前的渲染数据
    id_list     = []
    name_list   = []
    passwd_list = []
    type_list   = []
    state_list  = []

    userinfo = User.objects.filter(UserState='1')
    for i in userinfo:
        id_list.append(i.UserID)
        name_list.append(i.UserName)
        passwd_list.append(i.Password)
        type_list.append(i.UserType)
        state_list.append(i.UserState)

    user_info = []
    for (a,b,c,d,e) in zip(name_list,id_list,passwd_list,type_list,state_list):
        z = {}
        z['user_name']  = a
        z['user_id']    = b
        z['passwd']     = c
        z['user_type']  = d
        z['user_state'] = e
        user_info.append(z.copy())
   # user_info1 = json.dumps(user_info)

    if request.POST.get('user_add'):
        user_name   = request.POST.get('user_name','')
        user_id     = request.POST.get('user_id','')
        if User.objects.filter(UserName=user_name).exists():
            msg = '0001'  #账户名重复
            return HttpResponse(msg)

        elif User.objects.filter(UserID=user_id).exists():
            msg = '0010' #用户ID重复
            return HttpResponse(msg)

        try:
            user_type   = request.POST.get('user_type','')
            user_state  = request.POST.get('user_state','')
            passwd      = request.POST.get('passwd','')
            new_user    = User(UserName=user_name,Password=passwd,UserID=user_id,UserType=user_type,UserState=user_state)
            new_user.save()
            msg = '0000'
            return HttpResponse(msg)

        except:
            msg = '0011' #创建失败
            return HttpResponse(msg)

#删除用户AJAX
    elif request.POST.get('user_del'):
        user_id     = request.POST.get('user_id','')
        if User.objects.filter(UserID=user_id).exists():
                User.objects.filter(UserID=user_id).delete()
                msg = '0000'
                return HttpResponse(msg)
        else:
            msg = '0100'# 删除失败，请检查用户名和id是否正确，删除后页面需要刷新保证数据正确性
            return HttpResponse(msg)
#更新用户信息
    elif request.POST.get('user_update'):
        user_name   = request.POST.get('user_name','')
        user_id     = request.POST.get('user_id','')
        user_type   = request.POST.get('user_type','')
        user_state  = request.POST.get('user_state','')
        passwd      = request.POST.get('passwd','')
        try:
            User.objects.filter(UserName=user_name,UserID=user_id).update(Password=passwd,UserType=user_type,UserState=user_state)
            msg = '0000'
            return HttpResponse(msg)
        except:
            msg = '0101'  #更新失败，请检查用户名和id是否正确，更新后页面需要刷新保证数据正确性
            return HttpResponse(msg)
#查询用户信息
    elif  request.POST.get('user_query'):
        user_id     = request.POST.get('user_id','')
        user_obj = User.objects.filter(UserID=user_id)
        if user_obj.exists():
            user_info = {}
            user_info['name'] = user_obj[0].UserName
            user_info['id'] = user_obj[0].UserID
            user_info['passwd'] = user_obj[0].Password
            user_info['type'] = user_obj[0].UserType
            user_info['state'] = user_obj[0].UserState
            user_info['chinese_name'] = user_obj[0].UserNameCN
            #print user_info
            UserInfo = json.dumps(user_info)
            return HttpResponse(UserInfo)
        else:
            msg = '0111'
            return HttpResponse(msg)
    else:

        return render_to_response("salesman.html",locals())
