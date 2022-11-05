from django.shortcuts import render,HttpResponse
from .function.databaseOperations import *
from .variables.globalConstants import *
import json

# Create your views here.

# 注册
def log_up(request):

    return HttpResponse(json.dumps({'niha':'nihaosahi'}), content_type='application/json')

# 注销
def log_off(request):
    pass

# 修改手机号
def update_mobile(request):
    pass