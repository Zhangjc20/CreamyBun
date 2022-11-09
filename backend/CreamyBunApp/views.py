import os
import time

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .function.databaseOperations import *
from .variables.globalConstants import *
from .function.universalFunctions import *
import json


# Create your views here.

# 注册
def log_up(request):
    query_dict = request.GET
    type = query_dict.get("type", "")
    email = query_dict.get("email", "")
    username = query_dict.get("username", "")

    # 如果是发邮箱,verifyCode返回应该的验证码
    if type == 'getVerifyCode':
        check_user_exist_by_email = exist_user_by_email(email)
        if check_user_exist_by_email:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameEmail'}), content_type='application/json')
        verify_code = send_email(email)
        return HttpResponse(json.dumps({'status': 'ok', 'verifyCode': verify_code}), content_type='application/json')
        # return HttpResponse(json.dumps({'status':'ok'}), content_type='application/json')
    # 如果是点击注册
    elif type == 'logUp':
        #判断是否重名
        check_user_by_name = exist_user_by_name(username)
        if check_user_by_name:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'sameName'}), content_type='application/json')
        password = query_dict.get("password", "")
        create_user = add_a_user(username=username, password=password, email=email)
        if create_user:
            return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknown'}), content_type='application/json')
    
    # 未知操作
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}), content_type='application/json')


# 登录
def log_in(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    password = query_dict.get("password", "")

    # 用户是否存在
    is_user_exist = exist_user_by_name(username)
    if not is_user_exist:
        return HttpResponse(json.dumps({'status':'wrong','type':'noUser'}), content_type='application/json')
    
    # 密码是否正确
    is_password_right = match_username_with_password(username,password)
    if not is_password_right:
        return HttpResponse(json.dumps({'status':'wrong','type':'wrongPassword'}), content_type='application/json')
    
    return HttpResponse(json.dumps({'status':'ok'}), content_type='application/json')

# 重置密码
def reset_password(request):
    query_dict = request.GET
    reset_way = query_dict.get("resetWay", "") 
    password = query_dict.get("password", "") 
  
    # 如果是通过用户名重置
    if reset_way == 'username':
        # 用户是否存在
        username = query_dict.get("username", "")
        is_user_exist = exist_user_by_name(username)
        if is_user_exist:
            type = query_dict.get("type", "")
            if type == 'getVerifyCode':
                email = get_a_user_data(username).email
                verify_code = send_email(email)
                return HttpResponse(json.dumps({'status': 'ok', 'email':email, 'verifyCode': verify_code}), content_type='application/json')
            elif type == 'resetPassword':
                update_password_by_username(username,password)
                return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}), content_type='application/json')    
        else:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'noUser'}), content_type='application/json')

    # 如果是通过邮箱重置
    elif reset_way == 'email':
        # 用户是否存在
        email = query_dict.get("email", "")
        is_user_exist = exist_user_by_email(email)
        if is_user_exist:
            type = query_dict.get("type", "")
            if type == 'getVerifyCode':
                verify_code = send_email(email)
                return HttpResponse(json.dumps({'status': 'ok', 'verifyCode': verify_code}), content_type='application/json')
            elif type == 'resetPassword':
                update_password_by_email(email,password)
                return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'wrong', 'type': 'noUser'}), content_type='application/json')

    # 未知操作
    else:
        return HttpResponse(json.dumps({'status': 'wrong', 'type': 'unknownOperation'}), content_type='application/json')

# 获得个人基本信息
def get_user_basic_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    user_info = {
        'status':'ok',
        'userName':u.username,
        'mobileNumber':u.mobile_number,
        'donutNumber':u.donut_number,
        'email':u.email,
        'creditRank':u.credit_rank,
        'currentExp':u.current_exp,
        'expForUpgrade':get_exp_for_upgrade(u.credit_rank),
    }
    return HttpResponse(json.dumps(user_info), content_type='application/json')

# 获得奖励中心信息
def get_user_bonus_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    bonus_info = {
        'status':'ok',
        'donutToMoney':get_donut_to_money(),
        'moneyToDonet':get_money_to_donut(),
        'donutNumber':u.donut_number,
    }
    return HttpResponse(json.dumps(bonus_info), content_type='application/json')  

# 获得活动中心信息
def get_user_activity_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    activity_info = {
        'status':'ok',
        'continueSignInDays':u.continue_sign_in_days,
        'isTodaySignIn':u.is_today_sign_in,
    }
    return HttpResponse(json.dumps(activity_info), content_type='application/json')

# 获得设置信息
def get_user_settings_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    u = get_a_user_data(username)
    settings_info = {
        'status':'ok',
        'dark_mode':u.dark_mode,
    }
    return HttpResponse(json.dumps(settings_info), content_type='application/json')

# 获得已领取任务信息
# 任务信息(包括其id)通过列表传送,列表的每一项是一个字典
def get_user_received_task_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    # 
    # TODO
    # 

# 获得已发布任务信息
def get_user_released_task_info(request):
    query_dict = request.GET
    username = query_dict.get("username", "")
    # 
    # TODO
    # 


# 注销
def log_off(request):
    print(request.GET)
    pass


# 修改手机号
def update_mobile(request):
    pass


@csrf_exempt
def get_material_zip(request):
    if request.method == "POST":  # 判断接收的值是否为POST
        query_dict = request.POST
        print(query_dict)
        username = query_dict.get("username", "")
        file_type = query_dict.get("fileType", "")
        shard_index = eval(query_dict.get("shardIndex", ""))
        shard_total = eval(query_dict.get("shardTotal", ""))
        material_type = eval(query_dict.get("materialType", ""))
        current_time = query_dict.get("currentTime", "")
        dirname = username + '_' + current_time
        path = os.path.join("./cache", dirname)
        file = request.FILES['file']
        if not os.path.exists(path):  # 如果目录不存在就创建
            os.makedirs(path)
        path_name = os.path.join(path, "uploadPackage." + file_type)
        # time.sleep(0.5)
        handle_uploaded_file(file, path_name)
        print(shard_index, shard_total, query_dict)
        if shard_index == shard_total - 1:  # 此时要解压了
            unzip_file(path_name, path)
            os.remove(path_name)
            full_list, list_list = walk_file(path, material_type)
            # print(full_list)
            # print(list_list)
            return HttpResponse(json.dumps({'status': 'done', 'fullList': full_list, 'listList': list_list}),
                                content_type='application/json')
            pass
        # query_dict = request.POST
        # file = request.FILES.get('fileName', None)
        # myFile = request.FILES["file"]
        # print(myFile)
        # inp_files = request.FILES  # 上传文件的接收方式应该是request.FILES
        # file_obj = inp_files.get('f1')  # 通过get方法获取upload.html页面提交过来的文件
        # f = open(file_obj.name, 'wb')  # 将客户端上传的文件保存在服务器上，一定要用wb二进制方式写入，否则文件会乱码
        # for line in file_obj.chunks():  # 通过chunks分片上传存储在服务器内存中,以64k为一组，循环写入到服务器中
        #     f.write(line)
        # f.close()
    return HttpResponse(json.dumps({'status': 'next'}), content_type='application/json')


@csrf_exempt
def handle_release_action(request):
    if request.method == "POST":  # 判断接收的值是否为POST
        request_body = json.loads(request.body)
        print(request_body)
        act = request_body['act']
        msg_list = request_body['msgList']
        if act == 'delete':
            for target in msg_list:
                os.remove(target['filePath'])
    return HttpResponse(json.dumps({'status': 'done'}), content_type='application/json')


@csrf_exempt
def release_task(request):
    request_body = json.loads(request.body)
    print(request_body)
    return HttpResponse(json.dumps({'status': 'next'}), content_type='application/json')
