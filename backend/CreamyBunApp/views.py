from django.shortcuts import render,HttpResponse
from .function.databaseOperations import *
from .variables.globalConstants import *
import json

# Create your views here.

# 注册
def log_up(request):
    query_dict = request.GET
    type = query_dict.get("type","")
    #如果是发邮箱,verifyCode返回应该的验证码
    if type == 'getEmail':
        pass
        #return HttpResponse(json.dumps({'status':'ok','verifyCode':}), content_type='application/json')
        return HttpResponse(json.dumps({'status':'ok'}), content_type='application/json')
    email = query_dict.get("email","")
    username = query_dict.get("username","")
    #判断是否重名
    flag = exist_user(username)
    if flag:
        return HttpResponse(json.dumps({'status':'wrong','type':'sameName'}), content_type='application/json')
    password = query_dict.get("password","")
    flag = add_a_user(username=username,password=password,email=email)
    if flag:
        return HttpResponse(json.dumps({'status':'ok'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'status':'wrong','type':'unknown'}), content_type='application/json')

# 注销
def log_off(request):
    pass

# 修改手机号
def update_mobile(request):
    pass